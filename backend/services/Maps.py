import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_nearby_hospitals(lat, lng):
    # This reaches out to Google's real database
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=hospital&key={API_KEY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        # Simplify the data for our frontend
        return [{"name": h["name"], "address": h.get("vicinity")} for h in results[:5]]
    return []