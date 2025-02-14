import pytest

from imgFolder.tracking import FileTracker
from imgFolder.db_connection import DBConn



# monkey patch DBConn.query_files
@pytest.fixture
def mock_response(monkeypatch):
    def mock_query(self):
        return [
        {'file':'file_1', 'label':'comida'},
        {'file':'file_2', 'label':'bebida'},
        ]   

    monkeypatch.setattr(DBConn, "query_files", mock_query)


class TestFileTracker():
    
    def test_get_labels_01(self, mock_response):
        # Arrange
        tracker = FileTracker()
        true = ["comida", "bebida"]

        # Act
        res = tracker.get_all_labels()
        
        # Assert
        assert(true == res)


    def test_get_labels_02(self, monkeypatch):
        # Arrange
        # monkey patch DBConn.query_files
        def mock_query(self):
            return [
            {'file':'file_1', 'label':'móveis'},
            {'file':'file_2', 'label':'bebida'},
            ]

        monkeypatch.setattr(DBConn, "query_files", mock_query)

        tracker = FileTracker()
        true = ["móveis", "bebida"]

        # Act
        res = tracker.get_all_labels()
        
        # Assert
        assert(true == res)


    def test_get_label(self, mock_response):
        # Arrange
        tracker = FileTracker()
        true = "bebida"

        # Act
        res = tracker.get_label("file_2")
        
        # Assert
        assert(true == res)


    def test_get_label_error(self, mock_response):
        # Arrange
        tracker = FileTracker()
        
        # Act
        # Assert
        with pytest.raises(ValueError):
            res = tracker.get_label("file_3")