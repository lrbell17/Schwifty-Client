import argparse
from api_client.character_client import CharacterClient
from api_client.location_client  import LocationClient
from io_utils.csv_util import CsvUtil
from io_utils.character_csv_reader import CharacterCsvReader

# File paths for storing character and location data
CHARACTER_FILE_PATH = "data/characters.csv"
LOCATION_FILE_PATH = "data/locations.csv"


def fetch_data():
    # Fetch character and location information from API
    character_client = CharacterClient()
    location_client = LocationClient()

    print("Fetching character data...")
    characters = character_client.fetch_all()
    print("Fetching location data...")
    locations = location_client.fetch_all()

    # Write data to CSV files
    character_csv = CsvUtil(CHARACTER_FILE_PATH)
    location_csv = CsvUtil(LOCATION_FILE_PATH)

    print(f"Writing character data to {CHARACTER_FILE_PATH}...")
    character_csv.write(characters)
    print(f"Writing location data to {LOCATION_FILE_PATH}...")
    location_csv.write(locations)


def main():
    parser = argparse.ArgumentParser(description="Rick & Morty CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Init command
    init_parser = subparsers.add_parser("init", help="Fetch and store character/location data")

    # Get character command
    get_parser = subparsers.add_parser("characters", help="Get characters by ID or name")
    get_parser.add_argument("--id", type=int, help="Character ID")
    get_parser.add_argument("--name", type=str, help="Character name")

    args = parser.parse_args()

    if args.command == "init":
        fetch_data()
    elif args.command == "characters":
        character_csv_reader = CharacterCsvReader(CHARACTER_FILE_PATH, LOCATION_FILE_PATH)
        character_csv_reader.get_character(char_id=args.id, name=args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
