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


    def folder_exists(self, parent, folder):
        foldername = os.path.join(parent, folder)

        return os.path.exists(foldername)


    def get_files(self, foldername):

        # https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
        all_files = [f for f in os.listdir(foldername) if os.path.isfile(f)]

        # all_files = []
        # for subdir, dirs, files in os.walk(foldername):
        #     for file in files:
        #         all_files.append(file)

        return all_files