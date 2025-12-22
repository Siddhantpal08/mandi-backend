from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat
from app.config import ENV
from app.db.init_db import init_db

app = FastAPI(
    title="AI Mandi Intelligence Backend",
    description="Backend for Agriculture Decision Support System",
    version="0.1.0",
    docs_url="/docs" if ENV == "dev" else None,
    redoc_url=None
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ RUN DB INIT ON STARTUP
@app.on_event("startup")
def startup_event():
    init_db()

# Routes
app.include_router(chat.router, prefix="/chat")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "AI Mandi Intelligence Backend",
        "env": ENV
    }
