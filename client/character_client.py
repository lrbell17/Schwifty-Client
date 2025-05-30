from .api_client import ApiClient
import re

CHARACTER_ENDPOINT = "character"

class CharacterClient(ApiClient):

    def get_endpoint(self):
        return CHARACTER_ENDPOINT
    
    def parse_response(self, result):

        # Get location ID from $.location.url
        location = result.get("location", {})
        location_url = location.get("url", "")
        location_id = None
        match = re.search(r"/location/(\d+)", location_url)
        if match:
            location_id = int(match.group(1))

        return {
            "id": result.get("id"),
            "name": result.get("name"),
            "status": result.get("status"),
            "species": result.get("species"),
            "origin.name": result.get("origin", {}).get("name"),
            "location.id": location_id
        }
