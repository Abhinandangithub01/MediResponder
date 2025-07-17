# main.py

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
import asyncio
import websockets
import json
from dotenv import load_dotenv

load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

app = FastAPI()

# Allow all origins (dev mode)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MediResponder backend running!"}


@app.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Connect to AssemblyAI’s real-time endpoint
    async with websockets.connect(
        'wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000',
        extra_headers={"Authorization": ASSEMBLYAI_API_KEY},
    ) as assembly_ws:

        async def send_audio():
            while True:
                try:
                    audio_chunk = await websocket.receive_bytes()
                    await assembly_ws.send(audio_chunk)
                except Exception as e:
                    print("Audio stream closed", e)
                    break

        async def receive_transcripts():
            while True:
                try:
                    result = await assembly_ws.recv()
                    data = json.loads(result)
                    if "text" in data and data["message_type"] == "FinalTranscript":
                        await websocket.send_text(data["text"])
                except Exception as e:
                    print("Transcript stream closed", e)
                    break

        # Run both tasks in parallel
        await asyncio.gather(send_audio(), receive_transcripts())
