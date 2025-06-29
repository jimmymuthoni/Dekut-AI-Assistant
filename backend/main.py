from fastapi import FastAPI, Request, UploadFile, Form
from rag_pipeline import RAG
from speech_text import transcribe, synthesize
from whatsapp import TwilioWhatsApp

app = FastAPI()

# Initialize RAG pipeline and WhatsApp handler
rag = RAG()
wa = TwilioWhatsApp()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    """
    WhatsApp webhook handler.
    Receives messages from Twilio and responds using the RAG system.
    """
    data = await request.form()
    from_ = data["From"]
    body = data["Body"]

    response = await rag.answer(body)
    wa.send_message(from_, response)

    return {"status": "success", "message": "WhatsApp message processed"}

@app.post("/text_query")
async def text_query(q: str):
    """
    Endpoint for handling text queries from the Streamlit frontend.
    """
    answer = await rag.answer(q)
    return {"answer": answer}

@app.post("/voice_query")
async def voice_query(audio_file: UploadFile):
    """
    Endpoint for handling voice queries from the Streamlit frontend.
    Accepts uploaded audio file and returns both text and audio responses.
    """
    audio_bytes = await audio_file.read()
    text = transcribe(audio_bytes)
    answer = await rag.answer(text)
    audio_response = synthesize(answer)

    return {
        "answer": answer,
        "audio": audio_response
    }
