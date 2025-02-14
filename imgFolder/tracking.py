from imgFolder.db_connection import DBConn

class FileTracker:
	def __init__(self):
		self.folder = "."
		self.db_client = DBConn()

		# List of dicts
		self.current_files = self.db_client.query_files()


	def get_all_labels(self) -> list:
		labels = set()
		for file in self.current_files:
			labels.add(file['label'])

		return sorted(labels)


	def get_label(self, img_name):
		label = None
		for file in self.current_files:
			if file['file'] == img_name:
				label = file['label']

		if label == None:
			raise ValueError("No such file in the tracked list.")

		return label


	def set_label(self, img_name, label):
		# ask for the db connection to update the file
		self.db_client.update_db(
						uid=img_name, 
						field='label',
						value=label
						)