import os
from pathlib import Path

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


    def get_ext(self, file):
        return Path(file).suffix


    def _is_ext_in_list(self, file, ext_list=None):
        if ext_list is None:
            return True

        else:
            ext = self.get_ext(file)
            return ext in ext_list



    def get_files(self, foldername, subfolders=False, ext_list=None):

        if not subfolders:
            # https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
            all_files = [f for f in os.listdir(foldername) 
                         if os.path.isfile(f) 
                         and self._is_ext_in_list(f, ext_list)]

        else:
            all_files = []
            for subdir, dirs, files in os.walk(foldername):
                for file in files:
                    if self._is_ext_in_list(file, ext_list):
                        all_files.append(os.sep.join([subdir, file]))

        return all_files