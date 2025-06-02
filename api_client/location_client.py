from .client import RickAndMortyClient

LOCATION_ENDPOINT = "location"

class LocationClient(RickAndMortyClient):
    def get_endpoint(self):
        return LOCATION_ENDPOINT
    
    def parse_response(self, resp):
        return {
            "id": resp["id"], # required
            "name": resp.get("name"),
            "type": resp.get("type"),
            "dimension": resp.get("dimension")
        }
