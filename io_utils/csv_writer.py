import csv
import os

class CsvWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, records): 
        if not records:
            print("No records to write")
            return
        
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True) # create target directory if it doesn't exist

        header = records[0].keys()
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            
            for record in records:
                try:
                    writer.writerow(record)
                except Exception as e:
                    print(f"Unable to write record {record}: {e}")
