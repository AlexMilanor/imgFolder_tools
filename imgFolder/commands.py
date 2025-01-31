from imgFolder.controllers import LabelControl

def run_label_command(imgpath):
	label = input("Label: ")

	labeler = LabelControl(imgpath)
	payload = labeler._set_label(label)

	print(payload)
