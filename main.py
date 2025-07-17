from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "MediResponder backend running!"}

@app.post("/process")
async def process_message(request: MessageRequest):
    user_message = request.message
    return {"reply": f"Received: {user_message}. Help is on the way! 🚑"}
