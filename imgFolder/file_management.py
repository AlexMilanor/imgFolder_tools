import os

class FileManager:
    def __init__(self, folder):
        self.folder = folder

    def create_folder(self, parent, folder):
        foldername = os.path.join(parent, folder)

        if not os.path.exists(foldername):
            os.makedirs(foldername)
        else:
            raise ValueError("This folder already exists.")


    def create_file(self, parent, folder, file, content): 
        filename = os.path.join(parent, folder, file)
        with open(filename, 'w') as fp:
            fp.write(content)
