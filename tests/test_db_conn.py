import csv
import builtins
from io import StringIO

from imgFolder.db_connection import DBConn


class TestDBConn():
    
    def test_get_labels_01(self, monkeypatch):
        # Arrange
        # monkey patch csv.DictReader
        def mock_csv(file, mode):
            return StringIO(
            "arquivo,label,col3\n"
            "arq1,tag1,a\n"
            "arq2,tag2,b\n"
            "arq3,tag3,c\n"
            )

        monkeypatch.setattr(builtins, "open", mock_csv)
        conn = DBConn('.')

        true = [
                {"arquivo":"arq1", "label":"tag1", "col3":"a"},
                {"arquivo":"arq2", "label":"tag2", "col3":"b"},
                {"arquivo":"arq3", "label":"tag3", "col3":"c"},
        ]

        # Act
        res = conn.query_files()
        
        # Assert
        print(res)
        assert(true == res)

