from imgFolder.tracking import FileTracker


class LabelControl:
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.tracker = FileTracker()


    def set_label(self, label):    
        # Ask Tracker to set as the given label.
        self.tracker.set_label(self.imgpath, label)

        # Return the result
        new_label = self.tracker.get_label(self.imgpath)
        return {self.imgpath:new_label}


    def get_label(self):
        return self.tracker.get_label(self.imgpath)


    def get_all_labels(self):
        return self.tracker.get_all_labels()


    def check_file_tracked(self):
        self.tracker.check_file_tracked(self.imgpath)