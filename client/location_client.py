from .api_client import ApiClient

LOCATION_ENDPOINT = "location"

class LocationClient(ApiClient):
    def get_endpoint(self):
        return LOCATION_ENDPOINT
    
    def parse_response(self, resp):
        return {
            "id": resp["id"], # required
            "name": resp.get("name"),
            "type": resp.get("type"),
            "dimension": resp.get("dimension")
        }
