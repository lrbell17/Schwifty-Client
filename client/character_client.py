from .api_client import ApiClient
import re

CHARACTER_ENDPOINT = "character"

class CharacterClient(ApiClient):

    def get_endpoint(self):
        return CHARACTER_ENDPOINT
    
    def parse_response(self, result):

        # Get location ID from $.location.url
        location_url = result["location"]["url"]
        location_id = None
        match = re.search(r"/location/(\d+)", location_url)
        if match:
            location_id = int(match.group(1))
        else: 
            raise ValueError(f"Could not extract ID location URL: {location_url}")

        return {
            "id": result["id"], # required
            "name": result.get("name"),
            "status": result.get("status"),
            "species": result.get("species"),
            "origin.name": result.get("origin", {}).get("name"),
            "location.id": location_id
        }
