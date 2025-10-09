from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import time
import traceback

app = FastAPI()

# ---------------- SETUP STRUCTURED LOGGING ----------------
logging.basicConfig(
    filename="app.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


@app.middleware("http")
async def time_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["Process-Time"] = f"{process_time:.4f}"
    logging.info(f"Request: {request.url.path} took {process_time:.4f} seconds")
    return response


@app.get("/")
async def home():
    time.sleep(2.0)
    return JSONResponse(
        content={
            "message": "Request processed",
        }
    )
