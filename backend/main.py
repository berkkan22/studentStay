import os
from config import load_config
from fastapi import FastAPI, Request, status, Depends, HTTPException
from pydantic import BaseModel
import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader
import re
import psycopg2
import jwt
# from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, InvalidSignatureError
import requests
from dotenv import load_dotenv

config = load_config()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY_NAME = "X-TOKEN"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Endpoint for fetching the JWKS from Authentik
JWKS_URL = "https://auth.berkkan.de/application/o/hadith-api/jwks/"


def get_jwks():
    """Fetch the JWKS from the Authentik endpoint."""
    response = requests.get(JWKS_URL)
    if response.status_code == 200:
        return response.json()
    else:
        # logger.error(f"Failed to fetch JWKS: {
        #     response.status_code}, {response.json()}")
        raise Exception(f"Failed to fetch JWKS: {response.status_code}")


jwks = get_jwks()


def validate_jwt_token(jwt_token: str) -> bool:
    # Fetch the JWKS from Authentik

    # Decode the JWT header to get the 'kid' (Key ID)
    unverified_header = jwt.get_unverified_header(jwt_token)
    kid = unverified_header['kid']

    # Get the public key based on 'kid' from JWKS
    public_key = get_public_key(jwks, kid)

    # Verify the JWT with the public key
    # print("\n--- Verifying JWT with the public key ---")
    return verify_jwt(jwt_token, public_key)


def get_public_key(jwks, kid):
    """Extract the public key corresponding to the JWT's 'kid'."""
    for key in jwks['keys']:
        if key['kid'] == kid:
            return jwt.algorithms.RSAAlgorithm.from_jwk(key)
    # logger.error(f"Public key not found for kid: {kid}")
    raise Exception(f"Public key not found for kid: {kid}")


def verify_jwt(token, public_key):
    """Decode and verify the JWT using the public key."""
    try:
        unverified_token = decode_jwt_unverified(token)
        aud = unverified_token.get("aud")
        verified_token = jwt.decode(token, public_key, algorithms=[
                                    "RS256"], audience=aud, options={"verify_exp": True})
        # print("Verified Token Payload:", verified_token)
        return True
    except jwt.ExpiredSignatureError:
        # logger.error("Token has expired")
        return False
    except jwt.InvalidSignatureError:
        # logger.error("Invalid signature")
        return False
    except jwt.InvalidTokenError as e:
        # logger.error(f"Invalid token {e}")
        return False


def decode_jwt_unverified(token):
    return jwt.decode(token, options={"verify_signature": False})


def decode_jwt(token):
    # Fetch the JWKS from Authentik
    jwks = get_jwks()

    # Decode the JWT header to get the 'kid' (Key ID)
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header['kid']

    # Get the public key based on 'kid' from JWKS
    public_key = get_public_key(jwks, kid)

    unverified_token = decode_jwt_unverified(token)
    aud = unverified_token.get("aud")

    # Verify the JWT with the public key
    return jwt.decode(token, public_key, algorithms=["RS256"], audience=aud, options={"verify_exp": True})


async def get_api_key_http(api_key_header: str = Depends(api_key_header)):
    if api_key_header and validate_jwt_token(api_key_header):
        return api_key_header
    else:
        # logger.error("Invalid or missing API Key")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}


class User(BaseModel):
    firstname: str
    lastname: str
    birthday: datetime.date
    bafog: float
    rent: float
    home_entrance: datetime.date
    home_exit: datetime.date
    contract: datetime.date
    university: str
    course: str
    semester: str
    university_tr: str
    telephone: str
    email: str
    address: str


def clearSemester(sem):
    if sem is None:
        return None
    match = re.search(r'\d+', sem)
    if match:
        return int(match.group())
    print("No match found")
    return None


@app.post("/submit")
async def register_user(user: Request):
    try:
        user = await user.json()
        user = user["user"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO student (firstname, lastname, birthday, email, telephone, address, reason, university, course, semester, university_tr, bafog, company, others, submit_date, home_entrance, home_exit, contract, language_course, rent)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING id

        """, (
            user["firstname"], user["lastname"], user["birthday"], user["email"], user["telephone"], user["address"], user["reason"], user["university"], user["course"], clearSemester(
                user["semester"]), user.get("university_tr"), user.get("bafog"), user.get("company"), user.get("others"), datetime.datetime.now(), user.get("home_entrance"), user.get("home_exit"), user.get("contract"), user.get("sprachkurs"), user.get("rent")
        ))

        conn.commit()

        studentId = cur.fetchone()[0]

        if (user.get("wohnheim") and studentId):
            result = await update_student_room_intern(studentId, user.get("wohnheim"))
            print(result)

        cur.close()
        conn.close()

        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.get("/rooms")
async def get_rooms(api_key: str = Depends(get_api_key_http)):
    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM room
        """)

        rooms = cur.fetchall()

        cur.close()
        conn.close()

        return {"status": "success", "rooms": rooms}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.get("/students")
async def get_students(api_key: str = Depends(get_api_key_http)):
    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM student
        """)

        students = cur.fetchall()

        cur.close()
        conn.close()

        return {"status": "success", "students": students}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/updateStudentRoom")
async def update_student_room(data: Request, api_key: str = Depends(get_api_key_http)):
    try:
        data = await data.json()
        student_id = data["studentId"]
        room_location = data["roomId"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # get the next available room id for that location
        cur.execute("""
            SELECT r.id FROM room r
            LEFT JOIN student s ON r.id = s.room_id
            WHERE r.location = %s AND s.room_id IS NULL
        """, (room_location,))

        room = cur.fetchone()
        if room is not None:
            room_location = room[0]
        else:
            return {"status": "fail", "message": "No available room found for the given location"}

        cur.execute("""
            UPDATE student
            SET room_id = %s
            WHERE id = %s
        """, (room_location, student_id))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student room updated successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


async def update_student_room_intern(studentId, roomLocation):
    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # get the next available room id for that location
        cur.execute("""
            SELECT r.id FROM room r
            LEFT JOIN student s ON r.id = s.room_id
            WHERE r.location = %s AND s.room_id IS NULL
        """, (roomLocation,))

        room = cur.fetchone()
        if room is not None:
            roomLocation = room[0]
        else:
            print(f"Student with id {
                  studentId} wants to go into the room {roomLocation}")
            return {"status": "fail", "message": "No available room found for the given location"}

        cur.execute("""
            UPDATE student
            SET room_id = %s
            WHERE id = %s
        """, (roomLocation, studentId))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student room updated successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/setStudentPassiv")
async def set_student_passiv(data: Request, api_key: str = Depends(get_api_key_http)):
    try:
        data = await data.json()
        student_id = data["studentId"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            UPDATE student
            SET passiv = TRUE, room_id = NULL
            WHERE id = %s
        """, (student_id,))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student set to passive successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/setStudentAktiv")
async def set_student_aktiv(data: Request, api_key: str = Depends(get_api_key_http)):
    try:
        data = await data.json()
        student_id = data["studentId"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            UPDATE student
            SET passiv = FALSE, submit_date = NOW()
            WHERE id = %s
        """, (student_id,))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student set to active successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/updateStudent")
async def update_student(data: Request, api_key: str = Depends(get_api_key_http)):
    try:
        data = await data.json()
        student_id = data["studentId"]
        update_fields = data["updateFields"]

        if not update_fields:
            return {"status": "fail", "message": "No fields to update"}

        update_fields = {key: (None if value == '-' or value == '' else value)
                         for key, value in update_fields.items()}
        set_clause = ", ".join([f"{key} = %s" for key in update_fields.keys()])
        values = list(update_fields.values())
        values.append(student_id)

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute(f"""
            UPDATE student
            SET {set_clause}
            WHERE id = %s
        """, values)

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student updated successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/deleteStudent")
async def delete_student(data: Request, api_key: str = Depends(get_api_key_http)):
    try:
        data = await data.json()
        student_id = data["studentId"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM student WHERE id = %s
        """, (student_id,))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student deleted successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


class TokenRefreshRequest(BaseModel):
    refresh_token: str


@app.post("/refresh-token")
async def refresh_token(request: TokenRefreshRequest):
    # logger.info(f"Refreshing token: {request.refresh_token}")
    try:
        load_dotenv()

        response = requests.post("https://auth.berkkan.de/application/o/token/", data={
            "grant_type": "refresh_token",
            "refresh_token": request.refresh_token,
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
        })

        if response.status_code != 200:
            # logger.error(f"Failed to refresh token error: {response.json()}")
            raise HTTPException(status_code=response.status_code,
                                detail=f"Failed to refresh token error: {response.json()}")
        # logger.info(f"Token refreshed: {response.json()}")
        return response.json()
    except Exception as e:
        # logger.error(f"Failed to refresh token error: {e}, {response.json()}")
        raise HTTPException(status_code=500, detail=str(e))
