from time import sleep
import os

from imgFolder.db_connection import DBConn
from imgFolder.file_management import FileManager
from imgFolder.utils import config


class FileTracker:
    def __init__(self):
        self.folder = "."
        self.file_mgmt = FileManager('.')
        
        # Check if folder is tracked
        if self.is_folder_tracked():
            self._init_db_connection()


    def _init_db_connection(self):
        # Define a DB Connection
        self.db_client = DBConn(config.CONFIG_FOLDER)
        # List of dicts with files in the folder
        self.current_files = self.db_client.query_files()


    def check_file_tracked(self, filename):
        exists = False
        for file in self.current_files:
            if file['file'] == filename:
                exists = True

        if not exists:
            raise ValueError(f"File {filename} do not exists "
                              "or is not being tracked.")


    def is_folder_tracked(self):
        return self.file_mgmt.folder_exists(self.folder, config.CONFIG_FOLDER)


    def get_all_labels(self) -> list:
        labels = set()
        for file in self.current_files:
            label = file.get('label', '')
            if len(label) != 0:
                labels.add(file['label'])

        return sorted(labels)


    def get_label(self, img_name: str):
        self.check_file_tracked(img_name)

        label = None
        for file in self.current_files:
            if file['file'] == img_name:
                label = file.get('label', '')       


        return label


    def set_label(self, img_name, label):
        # ask for the db connection to update the file
        self.db_client.update_db(
                        uid=img_name, 
                        field='label',
                        value=label
                        )
        self.current_files = self.db_client.query_files()


    def set_tracked_folder(self):
        self.file_mgmt.create_folder(parent=self.folder, folder=config.CONFIG_FOLDER)

        self.file_mgmt.create_file(
            parent=self.folder, 
            folder=config.CONFIG_FOLDER, 
            file="index.txt",
            content="Images being tracked!"
        )
        
        self.file_mgmt.create_file(
            parent=self.folder, 
            folder=config.CONFIG_FOLDER, 
            file=config.DB_FILENAME,
            content=f"file,label"
        )

        self._init_db_connection()
        files = self.file_mgmt.get_files(self.folder)
        self.db_client.insert_db(files)

        print("Tracking this folder's images.")