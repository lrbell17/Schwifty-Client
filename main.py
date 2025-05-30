from client.character_client import CharacterClient
from client.location_client  import LocationClient
from io_utils.csv_writer import CsvWriter

def main():
    # Initialze API clients
    character_client = CharacterClient()
    location_client = LocationClient()
    
    # Get all locations and characters
    characters = character_client.fetch_all()
    locations = location_client.fetch_all()

    # Initialize CSV writers
    character_writer = CsvWriter("data2/characters.csv")
    location_writer = CsvWriter("data2/locations.csv")

    # Write to CSV
    character_writer.write(characters)
    location_writer.write(locations)

if __name__ == "__main__":
    main()
