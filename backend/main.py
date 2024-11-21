from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime
from fastapi.middleware.cors import CORSMiddleware


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


@app.post("/submit")
async def register_user(user: Request):
    try:
        user = await user.json()
        required_fields = ["firstname", "lastname", "birthday", "bafog", "rent", "home_entrance", "home_exit", "contract", "university", "course", "semester", "university_tr", "telephone", "email", "address"]
        
        for field in required_fields:
            if field not in user or user[field] is None:
                return {"status": "fail", "message": f"Field '{field}' is missing or empty"}

        # TODO: add postgresql
        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}
