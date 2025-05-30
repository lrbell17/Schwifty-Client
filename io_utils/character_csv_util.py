from .csv_util import CsvUtil
from .enricher import Enricher

class CharacterCsvUtil(CsvUtil):

    def __init__(self, character_file_path, location_file_path):
        super().__init__(character_file_path)
        self.location_enricher = Enricher(
            "location.id", 
            "id", 
            CsvUtil(location_file_path),
            "location")

    # Call read_with_filters from super class, then enrich with location details
    def read_with_filters(self, filters): 
        results = super().read_with_filters(filters)
        return self.location_enricher.enrich(results)
