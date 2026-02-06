from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.Maps import get_nearby_hospitals
from schemas.sos import SOSRequest

# --- DATABASE & MODELS ---
from database import models
from database.config import engine

# This creates the dharura.db file and tables automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DharuraPlus API")

# --- MIDDLEWARE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ROUTES ---

@app.get("/")
def read_root():
    return {
        "message": "DharuraPlus API is live!",
        "docs": "/docs",
        "status": "Healthy"
    }

@app.post("/sos")
async def trigger_sos(request: SOSRequest):
    # Extract coordinates from the request
    lat = request.location.get("lat")
    lng = request.location.get("lng")
    
    # Get real hospital data from Google Maps API via our service
    hospitals = get_nearby_hospitals(lat, lng)
    
    return {
        "status": "Success",
        "emergency_type": request.type,
        "location_received": {"lat": lat, "lng": lng},
        "recommended_hospitals": hospitals
    }