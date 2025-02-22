from time import sleep
import os

from imgFolder.db_connection import DBConn
from imgFolder.file_management import FileManager


class FileTracker:
    def __init__(self):
        self.folder = "."
        self.db_client = DBConn()
        self.file_mgmt = FileManager('.')

        # List of dicts
        self.current_files = self.db_client.query_files()


    def check_file_tracked(self, filename):
        exists = False
        for file in self.current_files:
            if file['file'] == filename:
                exists = True

        if not exists:
            raise ValueError(f"File {filename} do not exists "
                              "or is not being tracked.")


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
        config_folder = '.imgfolder'

        self.file_mgmt.create_folder(parent='.', folder=config_folder)
        self.file_mgmt.create_file(
            parent='.', 
            folder=config_folder, 
            file="index.txt",
            content="Images being tracked!"
        )

        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print("Tracking this folder's images.")