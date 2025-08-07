from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine
from . import models
from .dependencies import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL running"}

@app.post("/users/")
def create_user(username: str, email: str, role: str, db: Session = Depends(get_db)):
    new_user = models.User(username=username, email=email, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
