# Schwifty-Client

## Getting started

Required packages: 
- requests: `pip install requests`

## Extendability

### Adding fields
For the intended client (e.g. LocationClient), simply add fields to the **parse_response** method. Note that the fields must be extracted from the response body.
```
    def parse_response(self, result):
        
        # Add logic to extract more complex fields, if required

        return {
            "id": result.get("id"),
            "name": result.get("name"),
            "type": result.get("type"),
            "dimension": result.get("dimension"),
            # Additional fields here
        }

```

### Extending to other endpoints
Create new API client and implement the methods **get_endpoint** and **parse_response**.
```
class EpisodeClient(ApiClient):

    # Return the name of the endpoint (e.g. "episode") to be used in the URL
    def get_endpoint(self):
        ...
    
    # Return a dictionary of selected fields from the JSON response
    def parse_response(self, result):
        ...
```
Once complete, initialize the client and use **get_by_id** and **fetch_all** methods to get details.
```
episode_client = EpisodeClient()

episode_1 = episode_client.get_by_id(1)
all_episodes = episode_client.fetch_all()
```
