import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_nearby_hospitals(lat, lng):
    # If no key is set yet, keep returning mock data so code doesn't break
    if not API_KEY or API_KEY == "YOUR_KEY_HERE":
        return [{"name": "Mock Hospital (No API Key)", "distance": "0km"}]

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=hospital&key={API_KEY}"
    
    response = requests.get(url)
    results = response.json().get("results", [])
    
    hospitals = []
    for place in results[:3]: # Get the top 3 closest
        hospitals.append({
            "name": place.get("name"),
            "address": place.get("vicinity"),
            "rating": place.get("rating")
        })
    return hospitals