from app.db import models
from app.langchain.priority_agent import classify_email_priority
from datetime import datetime

async def save_and_classify_email(db, user_id: int, subject: str, body: str):
    priority_str = classify_email_priority(subject, body)
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    priority = priority_map.get(priority_str, 1)

    email = models.Email(
        subject=subject,
        body=body,
        priority=priority,
        timestamp=datetime.utcnow(),
        user_id=user_id
    )
    db.add(email)
    await db.commit()
    await db.refresh(email)
    return email
