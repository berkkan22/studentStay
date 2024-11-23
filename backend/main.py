from config import load_config
from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime
from fastapi.middleware.cors import CORSMiddleware
import re
import psycopg2

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


def clearSemester(sem: str):
    match = re.search(r'\d+', sem)
    if match:
        return int(match.group())
    return None


@app.post("/submit")
async def register_user(user: Request):
    try:
        user = await user.json()
        user = user["user"]
        required_fields = ["firstname", "lastname", "birthday", "bafog", "rent", "home_entrance", "home_exit",
                           "contract", "university", "course", "semester", "university_tr", "telephone", "email", "address"]

        for field in required_fields:
            if field not in user or user[field] is None:
                return {"status": "fail", "message": f"Field '{field}' is missing or empty"}

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO student (firstname, lastname, birthday, bafog, rent, home_entrance, home_exit, contract, university, course, semester, university_tr, telephone, email, address, submit_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            user["firstname"], user["lastname"], user["birthday"], user["bafog"], user["rent"], user["home_entrance"],
            user["home_exit"], user["contract"], user["university"], user["course"], clearSemester(
                user["semester"]),
            user["university_tr"], user["telephone"], user["email"], user["address"], datetime.datetime.now()
        ))

        conn.commit()

        cur.close()
        conn.close()

        # TODO: add postgresql
        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.get("/rooms")
async def get_rooms():
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
async def get_students():
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
async def update_student_room(data: Request):
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
        print(room)
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


@app.post("/setStudentPassiv")
async def set_student_passiv(data: Request):
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
async def set_student_aktiv(data: Request):
    try:
        data = await data.json()
        student_id = data["studentId"]

        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute("""
            UPDATE student
            SET passiv = FALSE
            WHERE id = %s
        """, (student_id,))

        conn.commit()

        cur.close()
        conn.close()

        return {"status": "success", "message": "Student set to active successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}


@app.post("/updateStudent")
async def update_student(data: Request):
    try:
        data = await data.json()
        student_id = data["studentId"]
        update_fields = data["updateFields"]
        print(update_fields)

        if not update_fields:
            return {"status": "fail", "message": "No fields to update"}

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
