from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings

llm = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY)

def classify_email_priority(subject: str, body: str) -> str:
    messages = [
        SystemMessage(content="You are an assistant that classifies emails as High, Medium, or Low priority."),
        HumanMessage(content=f"Subject: {subject}\nBody: {body}")
    ]
    response = llm(messages)
    return response.content.strip()
