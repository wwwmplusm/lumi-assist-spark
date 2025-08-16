"""FastAPI application entry point for the Lumi AI backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers import teacher, student, ai, auth

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lumi AI Backend")

# CORS Configuration to allow frontend to connect
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teacher.router)
app.include_router(student.router)
app.include_router(ai.router)
app.include_router(auth.router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Simple health-check endpoint."""

    return {"status": "ok"}
