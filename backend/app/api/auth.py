from fastapi import APIRouter, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password
from fastapi.concurrency import run_in_threadpool

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user_in:UserCreate,db:Annotated[AsyncSession,Depends(get_db)]):
    hash= await run_in_threadpool(hash_password,user_in.password)
    user = User(
        email=user_in.email,
        hashed_password=hash,
        full_name=user_in.full_name
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user