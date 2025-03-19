from imgFolder.tracking import FileTracker

class LabelControl:
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.tracker = FileTracker()


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
        return sorted(lista, key=lambda x:x[0])


    def check_file_tracked(self) -> bool:
        self.tracker.check_file_tracked(self.imgpath)



class IndexControl:
    def __init__(self):
        self.tracker = FileTracker()

    def start_tracking_folder(self):
        self.tracker.set_tracked_folder()