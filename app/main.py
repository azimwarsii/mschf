from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base
from . import models
from .dependencies import get_db

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers with error handling
try:
    from .routers import auth_router, users_router, oauth_router
    app.include_router(auth_router, prefix="/api/v1", tags=["auth"])
    app.include_router(users_router, prefix="/api/v1", tags=["users"])
    app.include_router(oauth_router, prefix="/api/v1", tags=["oauth"])
    print("✅ All routers loaded successfully")
except Exception as e:
    print(f"❌ Error loading routers: {e}")

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL running"}
