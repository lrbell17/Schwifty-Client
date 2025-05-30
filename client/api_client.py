import requests

BASE_URL = "https://rickandmortyapi.com/api"

class ApiClient:

    # Get the name of the endpoint to be used in the URL
    def get_endpoint(self):
        raise NotImplementedError
    
    # Parse response to extract selected fields 
    def parse_response(self):
        raise NotImplementedError
    
    # Get all entities for an endpoint
    def fetch_all(self):
        results = []
        url = f"{BASE_URL}/{self.get_endpoint()}"
        
        while url: # loop through each page of results
            response = self._fetch_url(url)
            results.extend(response.get("results", []))
            
            if not response:
                break

            url = response.get("info", {}).get("next") # get next page of results
            
        return [self._safe_parse(item) for item in results]

    
    # Get an entity by ID
    def get_by_id(self, id): 
        url = f"{BASE_URL}/{self.get_endpoint()}/{id}"
        response = self._fetch_url(url, id=id)
        
        if response:
            return self._safe_parse(response)


    # Helper to fetch URL with error handling
    def _fetch_url(self, url, id=None):
        try:
            resp = requests.get(url)
            resp.raise_for_status() # raise an exception if the status isn't successful
            
            return resp.json()
        
        except requests.exceptions.HTTPError as http_err:
            if resp.status_code == 404 and id is not None:
                print(f"{self.get_endpoint()} with id={id} not found.")
            else:
                print(f"HTTP error at {url}: {http_err}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
        return None

    # Helper to parse response with error handling
    def _safe_parse(self, item):
        try:
            return self.parse_response(item)
        except (KeyError, ValueError) as e:
            print(f"Failed to parse item {e!r}: {item}")
            return None
