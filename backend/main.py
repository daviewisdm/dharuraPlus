from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Add this
from services.Maps import get_nearby_hospitals
from schemas.sos import SOSRequest

app = FastAPI()

# --- ADD THIS PART ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows the frontend to talk to you
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------

@app.post("/sos")
async def trigger_sos(request: SOSRequest):
    hospitals = get_nearby_hospitals(request.location.get("lat"), request.location.get("lng"))
    return {
        "status": "Success",
        "emergency": request.type,
        "recommended_hospitals": hospitals
    }