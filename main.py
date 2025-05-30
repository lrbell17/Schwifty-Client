from client.character_client import CharacterClient
from client.location_client  import LocationClient

def main():
    character_client = CharacterClient()
    location_client = LocationClient()
    
    # characters = character_client.fetch_all()
    # print("Characters: ")
    # for c in characters:
    #     print(c)

    
    # locations = location_client.fetch_all()
    # print("\nLocations:")
    # for l in locations:
    #     print(l)

    print(f"Character 1: {character_client.get_by_id(1)}")
    print(f"Location 1: {location_client.get_by_id(256)}")

if __name__ == "__main__":
    main()
