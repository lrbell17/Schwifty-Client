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
            try:
                response = requests.get(url)
                response.raise_for_status() # raise an exception if the status isn't successful
                
                data = response.json()
                results.extend(data.get("results", []))
                
                url = data.get("info", {}).get("next") # get the URL for the next page of results

            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                
        return [self.parse_response(item) for item in results]
    
    # Get an entity by ID
    def get_by_id(self, id): 
        url = f"{BASE_URL}/{self.get_endpoint()}/{id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            return self.parse_response(data)

        except requests.exceptions.HTTPError as http_err:
            # Handle not found error
            if response.status_code == 404:
                print(f"{self.get_endpoint()} with id {id} not found")
            else:
                print(f"HTTP error at {url}: {http_err}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
