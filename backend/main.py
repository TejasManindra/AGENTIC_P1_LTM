
from fastapi import FastAPI

from backend.config import settings
from backend.routes.analysis import router as analysis_router
app = FastAPI(
    title=settings.app_name,
    description=(
        "AI-powered Business Intelligence and Strategic "
        "Recommendation System"
    ),
    version="0.1.0",
)
app.include_router(analysis_router)

@app.get("/")
def root():
    return {
        "message": "Agentic BI API is running",
        "status": "success",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }