import requests

def get_nearby_hospitals(lat, lng):
    # Overpass API is a free tool to query OpenStreetMap data
    # We are looking for 'amenity=hospital' within a 5000m radius of your lat/lng
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node["amenity"="hospital"](around:5000,{lat},{lng});
    out body;
    """
    
    try:
        response = requests.post(overpass_url, data={'data': overpass_query})
        if response.status_code == 200:
            data = response.json()
            elements = data.get("elements", [])
            
            # Extract names and locations
            hospitals = []
            for e in elements[:5]:
                name = e.get("tags", {}).get("name", "Unknown Hospital")
                # OSM usually provides street names in tags
                address = e.get("tags", {}).get("addr:street", "Nearby Location")
                hospitals.append({"name": name, "address": address})
            
            return hospitals
    except Exception as e:
        print(f"OSM Error: {e}")
        
    return []