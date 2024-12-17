from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import chat

app = FastAPI(title="Solana Assistant API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}