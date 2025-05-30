from .api_client import ApiClient
import re

CHARACTER_ENDPOINT = "character"

class CharacterClient(ApiClient):

    def get_endpoint(self):
        return CHARACTER_ENDPOINT
    
    def parse_response(self, resp):
        return {
            "id": resp["id"], # required
            "name": resp.get("name"),
            "status": resp.get("status"),
            "species": resp.get("species"),
            "origin.name": resp.get("origin", {}).get("name"),
            "location.id": self._extract_location_id(resp)
        }

    # Helper to get location ID from $.location.url
    def _extract_location_id(self, resp):
        location_url = resp["location"]["url"]
        location_id = None
        match = re.search(r"/location/(\d+)", location_url)
        if match:
            return int(match.group(1))
        else: 
            raise ValueError(f"Could not extract ID location URL: {location_url}")
