from imgFolder.db_connection import DBConn

class FileTracker:
    def __init__(self):
        self.folder = "."
        self.db_client = DBConn()

        # List of dicts
        self.current_files = self.db_client.query_files()


    def check_file_exists(self, filename):
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


    def get_label(self, img_name):
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