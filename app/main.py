from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.api import auth, emails
from app.core.config import settings

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(auth.router)
app.include_router(emails.router)

@app.get("/")
def root():
    return {"message": "Email prioritization agent running"}