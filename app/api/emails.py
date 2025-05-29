from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import session, models

router = APIRouter(prefix="/emails")

@router.get("/")
async def get_emails(user_id: int, db: AsyncSession = Depends(session.get_db)):
    result = await db.execute(select(models.Email).filter(models.Email.user_id == user_id))
    emails = result.scalars().all()
    return emails