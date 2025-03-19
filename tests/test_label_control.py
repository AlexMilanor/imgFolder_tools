import pytest

from imgFolder.controllers import LabelControl
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


class TestLabelControl():

    def test_get_all_imgs_labels(self, mock_response, mock_all):
        # Arrange
        true = [('bebida', 'file_2'), ('comida', 'file_1')]

        # Act
        labeler = LabelControl(imgpath=None)
        res = labeler.get_imgs_and_labels()

        # Assert
        assert(true == res)