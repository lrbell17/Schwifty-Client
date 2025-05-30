from .api_client import ApiClient

LOCATION_ENDPOINT = "location"

class LocationClient(ApiClient):
    def get_endpoint(self):
        return LOCATION_ENDPOINT
    
    def parse_response(self, result):
        return {
            "id": result["id"], # required
            "name": result.get("name"),
            "type": result.get("type"),
            "dimension": result.get("dimension")
        }
