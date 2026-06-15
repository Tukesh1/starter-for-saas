from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import router as api_router
from backend.app.core.config import settings
from backend.app.core.auth import verify_supabase_token

app = FastAPI(title="FLIPO-SAAS FastAPI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FLIPO-SAAS — AI SaaS Starter Backend"}

app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(verify_supabase_token)])
