import csv

class DBConn:
    def __init__(self):
        self.file = "./db_prototype.csv"

    def query_files(self) -> dict:
        with open(self.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            files_list = []
            for row in reader:
                files_list.append(row)
        
        return files_list
