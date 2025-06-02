# Schwifty-Client

A simple CLI tool to fetch, store, and query Rick and Morty character and location data using CSV files. Characters are automatically enriched with their corresponding location details for easier access and analysis.

## Getting started

#### Required packages
- requests: `pip install requests`
- pytest: `pip install pytest` (for testing only)

#### Usage
Run the CLI tool with the `init` command to load data from Rick and Morty API to CSV files. 
```
python cli.py init
```
Then, use the `characters` command to search for characters by id and/or name.
```
python cli.py characters --id 826
python cli.py characters --name "Rick Sanchez"
```
#### Testing

Run unit tests: `pytest -q`

## Extendability

### Adding fields
For the intended client (e.g. LocationClient), simply add fields to the **parse_response** method. Note that the fields must be extracted from the response body.
```
    def parse_response(self, resp):
        return {
            "id": resp.get("id"),
            "name": resp.get("name"),
            "type": resp.get("type"),
            "dimension": resp.get("dimension"),
            # Additional fields here
        }
```

### Extending to other endpoints
Create new API client and implement the methods **get_endpoint** and **parse_response**.
```
class EpisodeClient(RickAndMortyClient):

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

### Querying CSV by different fields
The **read_with_filters** method of CsvUtil accepts a dictionary of filters and returns a list containing all the matched records.
```
character_csv = CsvUtil(CHARACTER_FILE_PATH)
humans = character_csv.read_with_filters("species": "Human", "status": "Alive")
```

### Enriching CSV results
The **EnrichedCsvUtil** class can be used to support enrichment across multiple CSV files. 

Consider an example where we want to enrich character data with location data by matching the `origin.id` of the character to the `id` of the location: 

* **characters.csv**: id, name, status, species, origin\.id, location\.id
* **locations.csv**: id, name, type, dimension

```
enriched_character_csv = EnrichedCsvUtil(
    "characters.csv", 
    Enricher(
        "origin.id",              # The name of the character column to match
        "id",                     # The name of the location column to match (this is assumed to be unique)
        CsvUtil("locations.csv"), # CSV utility to read location data
        "origin"                  # The name of the key to store the object in the result
    )
)
```
Now, calling the **read_with_filters** method on the CSV utility will return the character automatically enriched with the origin data.
```
enriched_character_csv.read_with_filters("id": 1)
```
Result:
```
[
    {
        "id": 1,
        "name": "Rick Sanchez",
        "status": "Alive",
        "species": "Human",
        "location.id": "3",
        "origin": {
            "id": "1",
            "name": "Earth (C-137)",
            "type: "Planet",
            "dimension": "Dimension C-137"
        }
    }
]
```