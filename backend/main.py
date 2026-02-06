from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.Maps import get_nearby_hospitals
from schemas.sos import SOSRequest

# --- NEW DATABASE IMPORTS ---
from database import models
from database.config import engine

# This line tells SQLAlchemy to create the tables in dharura.db
models.Base.metadata.create_all(bind=engine)
# ----------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sos")
async def trigger_sos(request: SOSRequest):
    hospitals = get_nearby_hospitals(request.location.get("lat"), request.location.get("lng"))
    return {
        "status": "Success",
        "emergency": request.type,
        "recommended_hospitals": hospitals
    }