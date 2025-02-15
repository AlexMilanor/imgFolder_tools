import csv
from copy import copy

class DBConn:
    def __init__(self):
        self._file = "./data/db_prototype.csv"
        self._schema = ['file', 'label']


    def query_files(self) -> dict:
        with open(self._file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            files_list = []
            for row in reader:
                files_list.append(row)
        
        return files_list


    def _change_file_list(
            self, uid: str, field: str, value: str
        ):

        if field not in self._schema:
            raise ValueError(f"Unknown field {field}")
        
        files_list = self.query_files()

        new_files_list = []
        for file in files_list:

            row = copy(file)
            if file['file'] == uid:
                row[field] = value

            new_files_list.append(row)

        return new_files_list



    def update_db(self, 
                  uid: str, 
                  field: str,
                  value: str,
        ) -> None:
        
        update_list = self._change_file_list(uid, field, value)

        with open(self._file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._schema)
            writer.writeheader()

            for row in update_list:
                writer.writerow(row)

