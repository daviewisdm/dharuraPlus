from pydantic import BaseModel
from typing import Dict

class SOSRequest(BaseModel):
    type: str          # e.g., "Epilepsy"
    location: Dict[str, float]  # e.g., {"lat": -1.2, "lng": 36.8}