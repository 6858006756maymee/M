from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    nickname TEXT PRIMARY KEY,
    counter INTEGER
)
""")
conn.commit()

class User(BaseModel):
    nickname: str

@app.post("/api/quiz/start")
def start_quiz(user: User):

    cur.execute("SELECT counter FROM users WHERE nickname=%s", (user.nickname,))
    result = cur.fetchone()

    if result:
        counter = result[0] + 1
        cur.execute(
            "UPDATE users SET counter=%s WHERE nickname=%s",
            (counter, user.nickname)
        )
    else:
        counter = 1
        cur.execute(
            "INSERT INTO users VALUES (%s,%s)",
            (user.nickname, counter)
        )

    conn.commit()

    return {"counter": counter}

@app.get("/health")
def health():
    return {"status": "ok"}
