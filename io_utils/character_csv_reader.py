import json
from .csv_util import CsvUtil
from .csv_util import EnrichedCsvUtil
from .enricher import Enricher

# Provides method to query character data by ID and/or name, enriched with location
class CharacterCsvReader():

    def __init__(self, character_file_path, location_file_path):
        self.character_csv = EnrichedCsvUtil(
            character_file_path, 
            Enricher("location.id", "id", CsvUtil(location_file_path), "location")
        )

    def get_character(self, char_id=None, name=None):
        if not char_id and not name:
            print("Error: Must provide either --id or --name.")
            return

        filters = {}
        if char_id:
            filters["id"] = str(char_id)
        if name:
            filters["name"] = name

        results = self.character_csv.read_with_filters(filters)

        if not results:
            print("No matching characters found.")
        else:
            print(json.dumps(results, indent=2))
