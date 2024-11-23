import datetime
from fastapi import FastAPI, HTTPException, Request
from config import load_config
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import requests
from dotenv import load_dotenv
import os


app = FastAPI()
config = load_config()
load_dotenv()

url = os.getenv("discord_webhook_url")

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
    return {"message": "running"}


def sendDiscordMessage(name, vorname, moschee, alter, email, handynummer):
    data = {}

    data["embeds"] = [
        {
            "description": "Name: " + name + "\nVorname: " + vorname + "\nMoschee: " + moschee + "\nAlter: " + str(alter) + "\nEmail: " + email + "\nHandynummer: " + handynummer,
            "title": "Neue Anmeldung",
        }
    ]
    requests.post(url, json=data)


@app.post("/submit")
async def submit_data(request: Request):
    data = await request.json()

    # Check if all required fields are present
    required_fields = ["name", "vorname",
                       "moschee", "alter", "email", "handynummer"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(
                status_code=400, detail=f"Missing field: {field}")

    name = data["name"]
    vorname = data["vorname"]
    moschee = data["moschee"]
    alter = data["alter"]
    email = data["email"]
    handynummer = data["handynummer"]

    try:
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL database")

        cursor = conn.cursor()

        # Insert data into the database
        cursor.execute(
            f"INSERT INTO registered (name, vorname, moschee, alter, email, handynummer, registration_date) VALUES ('{name}', '{vorname}', '{moschee}', {alter}, '{email}', '{handynummer}', '{datetime.datetime.now()}')")

        conn.commit()

        cursor.close()
        conn.close()

        sendDiscordMessage(
            name, vorname, moschee, alter, email, handynummer)

        return {"status": "submitted"}

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400, detail="Problem occured while inserting data into the database " + str(e))
