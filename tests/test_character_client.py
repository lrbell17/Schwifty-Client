from api_client.character_client import CharacterClient
import pytest

client = CharacterClient()

payload_valid = {
    "id": 1,
    "name": "Rick Sanchez",
    "status": "Alive",
    "species": "Human",
    "origin": {
        "name": "Earth (C-137)",
        "url": "https://rickandmortyapi.com/api/location/1"
    },
    "location": {
        "name": "Citadel of Ricks",
        "url": "https://rickandmortyapi.com/api/location/3"
    }
}

def test_parse_valid():
    parsed = client.parse_response(payload_valid)

    assert parsed["id"] == 1
    assert parsed["name"] == "Rick Sanchez"
    assert parsed["status"] == "Alive"
    assert parsed["species"] == "Human"
    assert parsed["origin.name"] == "Earth (C-137)"
    assert parsed["location.id"] == 3

payload_missing_id = {
    "name": "Rick Sanchez",
    "status": "Alive",
    "species": "Human",
    "origin": {
        "name": "Earth (C-137)",
        "url": "https://rickandmortyapi.com/api/location/1"
    },
    "location": {
        "name": "Citadel of Ricks",
        "url": "https://rickandmortyapi.com/api/location/3"
    }
}

def test_parse_missing_id():
    with pytest.raises(KeyError, match="id"):
        client.parse_response(payload_missing_id)
