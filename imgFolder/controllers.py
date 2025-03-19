import os

from imgFolder.tracking import FileTracker

class LabelControl:
    def __init__(self, imgpath):
        self.imgpath = self._adjust_imgpath(imgpath)
        self.tracker = FileTracker()


    def _adjust_imgpath(self, imgpath):
        if imgpath is None:
            return imgpath
        else:
            path = imgpath.lstrip(os.sep)
            root = path[:path.index(os.sep)] if os.sep in path else path
            if root != '.':
                return os.sep.join(['.', imgpath])
            else:
                return imgpath


    def set_label(self, label) -> None:    
        # Ask Tracker to set as the given label.
        self.tracker.set_label(self.imgpath, label)


    def get_label(self) -> str:
        return self.tracker.get_label(self.imgpath)


    def get_all_labels(self) -> list:
        all_labels = self.tracker.get_all_labels()
        return sorted(all_labels)


    def get_imgs_and_labels(self) -> dict:
        all_files = self.tracker.get_imgs_and_labels()
        lista = [(file['label'], file['file']) for file in all_files]
        empty_lista = [(file[0], file[1]) for file in lista if len(file[0]) == 0]
        fill_lista = sorted([(file[0], file[1]) for file in lista if len(file[0])!=0])

        return fill_lista + empty_lista


    def check_file_tracked(self) -> bool:
        self.tracker.check_file_tracked(self.imgpath)



class IndexControl:
    def __init__(self):
        self.tracker = FileTracker()

    def start_tracking_folder(self):
        self.tracker.set_tracked_folder()