import csv
import os

class CsvReadWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    # Write all records to a CSV file
    def write(self, records): 
        if not records:
            print("No records to write")
            return
        
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True) # create target directory if it doesn't exist

        header = records[0].keys()
        try:
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                
                for record in records:
                    try:
                        writer.writerow(record)
                    except Exception as e:
                        print(f"Unable to write record {record}: {e}")
        
        except Exception as e:
            print(f"Error opening file {self.file_path}: {e}")


    # Read a CSV file and return records matching provided filters
    def read_with_filters(self, filters):
        matched_records = []

        try: 
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames

                self._validate_columns(filters, headers)

                # Find records matching all filters
                for row in reader:
                    if all(row.get(key) == str(value) for key, value in filters.items()):
                        matched_records.append(row)

        except Exception as e:
            print(f"Error reading file {self.file_path}: {e}")
        
        return matched_records
    
    # Helper to make sure the filters provided match the CSV headers
    def _validate_columns(self, filters, headers):
        invalid_keys = [key for key in filters if key not in headers]
        if invalid_keys:
                raise ValueError(f"Invalid filter keys: {invalid_keys}. Valid headers are: {headers}")

