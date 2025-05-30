from client.character_client import CharacterClient
from client.location_client  import LocationClient
from io_utils.csv_io import CsvReadWriter


def main():
    # Initialze API clients
    character_client = CharacterClient()
    location_client = LocationClient()
    
    # Get all locations and characters
    characters = character_client.fetch_all()
    locations = location_client.fetch_all()

    # Initialize CSV writers
    character_rw = CsvReadWriter("data/characters.csv")
    location_rw = CsvReadWriter("data/locations.csv")

    # Write to CSV
    character_rw.write(characters)
    location_rw.write(locations)

    # Grab records from CSVs, applying filters
    ricks = character_rw.read_with_filters({"name": "Rick Sanchez", "status": "Alive"})
    print("Ricks:")
    for r in ricks: 
        print(r)

    stations = location_rw.read_with_filters({"type": "Space station"})
    print("\nStations:")
    for s in stations:
        print(s)

if __name__ == "__main__":
    main()
