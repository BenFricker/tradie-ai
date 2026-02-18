# Main Application File

# Import relevant modules
from fastapi import FastAPI, Request, Response
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Tradie AI is running"}

@app.post("/voice")
async def voice(request: Request):
    """Handle incoming calls from Twilio"""
    response = VoiceResponse()
    response.say(
        "G'day Mate! This is Polly Nicole from Tradie Assistance. This is a test call for the Tradie Assistant Service. Here is a little bit more talking to hear the voice. Goodbye.",
        voice="Polly.Nicole"
    )
    return Response(content=str(response), media_type="application/xml")

