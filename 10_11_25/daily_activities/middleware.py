import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("smart_query_logger")
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def setup_middleware(app):

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        logger.info(f"Incoming request: {request.method} {request.url}")
        try:
            response = await call_next(request)
            logger.info(f"Response status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return JSONResponse(status_code=500, content={"error": "Internal Server Error"})
