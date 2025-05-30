from client.character_client import CharacterClient
from client.location_client  import LocationClient
from io_utils.csv_util import CsvUtil
from io_utils.character_csv_util import CharacterCsvUtil

# Define paths for storing character and location data
CHARACTER_FILE_PATH = "data/characters.csv"
LOCATION_FILE_PATH = "data/locations.csv"

def main():
    # Initialize API clients for characters and locations
    character_client = CharacterClient()
    location_client = LocationClient()
    
    # Fetch all characters and locations from the API
    characters = character_client.fetch_all()
    locations = location_client.fetch_all()

    # Create CSV utilities to handle read/write operations
    character_csv = CsvUtil(CHARACTER_FILE_PATH)
    location_csv = CsvUtil(LOCATION_FILE_PATH)

    # Write to CSV
    character_csv.write(characters)
    location_csv.write(locations)

    # Grab records from CSVs, applying filters
    ricks = character_csv.read_with_filters({"name": "Rick Sanchez", "status": "Alive"})
    print("Filtered character data:")
    for r in ricks: 
        print(r)

    stations = location_csv.read_with_filters({"type": "Space station"})
    print("\nFiltered location data:")
    for s in stations:
        print(s)

    # Use custom CSV utility to read characters enriched with location data
    enriched_character_csv = CharacterCsvUtil(CHARACTER_FILE_PATH, LOCATION_FILE_PATH)
    print("\nEnriched character (ID = 1):")
    print(enriched_character_csv.read_with_filters({"id": 1}))

if __name__ == "__main__":
    main()
