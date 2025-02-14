from imgFolder.controllers import LabelControl
from imgFolder.tracking import FileTracker
from imgFolder.utils import color_text

def view_choices(choices, title="Choices", color='cyan', disp='bold'):
	print(
		color_text.design_text(
			title, color=color, display=disp
		)
	)
	for choice in choices:
		print(color_text.design_text(f"- {choice}", display='bold'))
	print("")


def run_label_command(imgpath):
	tracker = FileTracker()
	view_choices(tracker.get_all_labels(), title='Existing labels', disp='negative')

	label = input("Label: ")

	labeler = LabelControl(imgpath)
	payload = labeler.set_label(label)

	print(payload)
