import csv
from copy import copy
from pathlib import Path

from imgFolder.utils import config 

class DBConn:
    def __init__(self, path):
        db_path = Path(path)
        self._file = db_path / config.DB_FILENAME
        self._schema = ['file', 'label']


    def query_files(self) -> list:
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


    def insert_db(
            self,
            uid_list: list[str]
            ) -> None:

        insert_list = [{'file':uid, 'label':None} for uid in uid_list]
        with open(self._file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self._schema)
            writer.writeheader()

            for row in insert_list:
                writer.writerow(row)