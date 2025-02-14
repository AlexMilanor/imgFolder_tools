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



