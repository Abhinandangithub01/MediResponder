from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to call backend
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

# ✅ Correct POST route to handle messages
@app.post("/process")
async def process_message(request: MessageRequest):
    user_message = request.message

    # Simulate a response for now
    response_text = "Got it! Help is on the way 🚑"

    return {"reply": response_text}
