from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect (CORS settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MediResponder backend running!"}

# Add a route to test if AssemblyAI integration works
@app.post("/process")
async def process_message(request: Request):
    data = await request.json()
    user_msg = data.get("message", "")
    
    # Simulate response (you'll connect this to AssemblyAI later)
    return {"reply": f"Emergency noted: '{user_msg}'. Help is being arranged!"}
