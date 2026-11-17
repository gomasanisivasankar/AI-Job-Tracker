from fastapi import FastAPI,Depends
from app.core.config import settings
from typing import Annotated
from datetime import datetime
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text 


app = FastAPI(title=settings.app_name)


@app.get("/")
async def home():
    return {"message": "Welcome to Job Tracker API!"} 

@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    await db.execute(text("SELECT 1"))
    return {"status": "ok","database": "connected"}


@app.get("/about")
async def about():
    return {"app": "Job Tracker API ","version": "1.0.0", "description": "This API allows users to track job applications and their statuses."}

async def get_time():
    return datetime.now().strftime("%H:%M:%S")

@app.get("/time")
async def show_time(now: Annotated[str, Depends(get_time)]):
    return {"time": now}

@app.get("/greetings")
async def greetings(now: Annotated[str, Depends(get_time)]):
    return {"message": f"Hello, it is {now}!"}
