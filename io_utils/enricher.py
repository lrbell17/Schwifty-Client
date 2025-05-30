
class Enricher:

    """
    src_col: column in the source record (e.g. 'location.id')
    dest_col: column in the destination record (e.g. 'id')
    dest_csv_util: instance of CsvUtil for destination data
    nested_key: name of the nested field in the enriched record (e.g. 'location')
    """
    def __init__(self, src_col, dest_col, dest_csv_util, nested_key):
        self.src_key = src_col
        self.dest_key = dest_col
        self.dest_csv_util = dest_csv_util
        self.nested_key = nested_key

    # Enrich records with other entities by matching keys
    def enrich(self, records):
        enriched = []

        for record in records:
            
            # Get the value from source record we want to match with dest record
            src_value = record.get(self.src_key)
            if src_value is None:
                enriched.append(record)
                continue
            
            # Try to find the matching dest records
            try:
                matches = self.dest_csv_util.read_with_filters({self.dest_key: src_value})
            except Exception as e:
                print(f"Error filtering destination data: {e}")
                enriched.append(record)
                continue

            # If there's a matching record, enrich the source record with it
            if matches:
                dest_data = matches[0]  # Assuming one match
                enriched_record = record.copy()
                enriched_record[self.nested_key] = dest_data
                enriched_record.pop(self.src_key) # delete the source key

                enriched.append(enriched_record)
            else:
                enriched.append(record)
            
        return enriched
