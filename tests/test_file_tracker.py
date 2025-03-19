import pytest

from imgFolder.tracking import FileTracker
from imgFolder.db_connection import DBConn
from imgFolder.file_management import FileManager
from imgFolder.utils import config


# monkey patch DBConn.query_files
@pytest.fixture
def mock_response(monkeypatch):
    def mock_query(self):
        return [
        {'file':'file_1', 'label':'comida'},
        {'file':'file_2', 'label':'bebida'},
        ]   

    monkeypatch.setattr(DBConn, "query_files", mock_query)


# monkey patch FileManager.folder_exists
# monkey patch config.CONFIG_FOLDER
@pytest.fixture
def mock_all(monkeypatch):
    monkeypatch.setattr(FileManager, "folder_exists", lambda x, y, z: True)
    monkeypatch.setattr(config, "CONFIG_FOLDER", '.')    


class TestFileTracker():
    
    def test_get_all_labels_01(self, mock_response, mock_all):
        # Arrange
        tracker = FileTracker()
        true = ["bebida", "comida"]

        # Act
        res = tracker.get_all_labels()
        
        # Assert
        assert(true == res)


    def test_get_all_labels_02(self, monkeypatch, mock_all):
        # Arrange
        # monkey patch DBConn.query_files
        def mock_query(self):
            return [
            {'file':'file_1', 'label':'móveis'},
            {'file':'file_2', 'label':'bebida'},
            ]

        monkeypatch.setattr(DBConn, "query_files", mock_query)

        true = ["bebida", "móveis"]


        # Act
        tracker = FileTracker()
        res = tracker.get_all_labels()
        
        # Assert
        assert(true == res)


    def test_get_label(self, mock_response, mock_all):
        # Arrange
        tracker = FileTracker()
        true = "bebida"

        # Act
        res = tracker.get_label("file_2")
        
        # Assert
        assert(true == res)


    def test_get_label_error(self, mock_response, mock_all):
        # Arrange
        tracker = FileTracker()
        
        # Act
        # Assert
        with pytest.raises(ValueError):
            res = tracker.get_label("file_3")