import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers import citizen, volunteer, dashboard, recommendation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Climate RADAR API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendation.router)
app.include_router(citizen.router)
app.include_router(volunteer.router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"ok": True, "name": "Climate RADAR API"}
