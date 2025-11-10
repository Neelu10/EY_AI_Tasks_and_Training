from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os, json, httpx
from pathlib import Path


load_dotenv()
app = FastAPI(title="OpenRouter Q&A Assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-7b-instruct")
HISTORY_FILE = Path("qa-history.json")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env file")

class Prompt(BaseModel):
    topic: str
    question: str

@app.get("/")
async def home():
    """Serve frontend HTML"""
    return FileResponse("static/index.html")


@app.post("/generate")
async def generate_response(prompt: Prompt):
    """Generate an answer using OpenRouter's API"""

    if not prompt.topic.strip() or not prompt.question.strip():
        raise HTTPException(status_code=400, detail="Topic and question cannot be empty.")


    combined_query = f"Topic: {prompt.topic}\nQuestion: {prompt.question}"
    user_prompt = (
        f"The user is asking about the topic '{prompt.topic}'. "
        f"Answer the question clearly, factually, and concisely: {prompt.question}. "
        f"If comparison is required, highlight key differences with examples."
    )

    payload = {
        "model":"mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant specialized in technical and analytical explanations. "
                    "Always stay on-topic, provide factual information, and avoid unrelated answers. "
                    "If the user asks for a comparison, explicitly list differences between items."
                ),
            },
            {"role": "user", "content": user_prompt},
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "AI Knowledge Assistant"
    }

    try:
        async with httpx.AsyncClient(timeout=40.0) as client:
            response = await client.post(API_URL, headers=headers, json=payload)
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)

            result = response.json()
            answer = result["choices"][0]["message"]["content"]


            entry = {"topic": prompt.topic, "question": prompt.question, "answer": answer}

            if HISTORY_FILE.exists():
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = []


            data.append(entry)
            if len(data) > 10:
                data = data[-10:]

            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            return JSONResponse(content={"response": answer})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/history")
async def get_history():
    """Fetch saved Q&A history"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {"history": data}
    return {"history": []}
