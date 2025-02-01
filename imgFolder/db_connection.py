

class DBConn:
    def __init__(self):
        pass

    def query_files(self) -> dict:
        return [
            {"file":"file_1", "label":"label_1"},
            {"file":"file_2", "label":"label_2"},
        ]