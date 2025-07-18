from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.db import engine, SessionLocal
from app.models import Note

app = FastAPI()


@app.get("/notes")
def read_notes():
    db: Session = SessionLocal()
    notes = db.query(Note).all()
    return notes