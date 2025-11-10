from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from middleware import setup_middleware
from utils import process_query
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Smart Query AI")

# Middleware for logging & errors
setup_middleware(app)

# Allow Streamlit & Postman access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-7b-instruct")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env file")

class QueryRequest(BaseModel):
    query: str


@app.get("/")
async def home():
    return {"message": "Smart Query API is running!"}


@app.post("/ask")
async def ask_query(request: QueryRequest):
    try:
        answer = process_query(request.query)
        return {"query": request.query, "answer": answer, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
