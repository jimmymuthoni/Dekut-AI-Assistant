from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse
from rag_pipeline import RAG
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

# Twilio Configuration
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_SID, TWILIO_TOKEN)

# Initialize FastAPI Router
router = APIRouter()
rag = RAG()

@router.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    """
    WhatsApp webhook to receive and respond to messages via Twilio.
    """
    try:
        answer = await rag.answer(Body)
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=answer,
            to=From
        )

        return PlainTextResponse("Message processed", status_code=200)

    except Exception as e:
        print(f"Error: {e}")
        return PlainTextResponse(f"Error: {str(e)}", status_code=500)
