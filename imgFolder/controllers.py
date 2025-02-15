from imgFolder.tracking import FileTracker

class LabelControl:
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.tracker = FileTracker()


    def set_label(self, label):
        
        # Get image current label from Tracker, if exists.
        old_label = self.tracker.get_label(self.imgpath)
        
        # Ask Tracker to set as the given label.
        self.tracker.set_label(self.imgpath, label)

        # Return the result
        return {self.imgpath:label}


    def get_label(self):
        return self.tracker.get_label(self.imgpath)


    def get_all_labels(self):
        return self.tracker.get_all_labels()


    def check_file_tracked(self):
        self.tracker.check_file_exists(self.imgpath)
