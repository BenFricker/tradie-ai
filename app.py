# Main Application File

# Import relevant modules
from fastapi import FastAPI, Request, Response
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"message": "Tradie AI is running"}

@app.post("/voice")
async def voice(request: Request):
    """Handle incoming calls from Twilio with AI-generated greeting"""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly Australian tradie assistant. Generate a breif, casual greeting (max 20 words) for someone calling a builder's phone",},
            {"role": "user", "content": "Generate a greeting for this call"}
        ]
    )

    ai_greeting = completion.choices[0].message.content

    response = VoiceResponse()
    response.say(
        ai_greeting,
        voice="Polly.Nicole"
    )

    return Response(content=str(response), media_type="application/xml")
