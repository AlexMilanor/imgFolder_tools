from imgFolder.db_connection import DBConn

class FileTracker:
	def __init__(self):
		self.folder = "."
		self.db_client = DBConn()

	def get_labels(self):
		labels = [file['label'] for file in self.db_client.query_files()]
		return labels