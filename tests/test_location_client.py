from client.location_client import LocationClient
import pytest

client = LocationClient()

payload_valid = {
    "id": 1,
    "name": "Earth (C-137)",
    "type": "Planet",
    "dimension": "Dimension C-137"
}

def test_parse_valid():
    parsed = client.parse_response(payload_valid)

    assert parsed["id"] == 1
    assert parsed["name"] == "Earth (C-137)"
    assert parsed["type"] == "Planet"
    assert parsed["dimension"] == "Dimension C-137"


payload_missing_id = {
    "name": "Earth (C-137)",
    "type": "Planet",
    "dimension": "Dimension C-137"
}

def test_parse_missing_id():
    with pytest.raises(KeyError, match="id"):
        client.parse_response(payload_missing_id)
