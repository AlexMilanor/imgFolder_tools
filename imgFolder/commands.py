from imgFolder.controllers import LabelControl
from imgFolder.utils import color_text

def view_choices(choices, title="Choices", color='cyan', disp='bold'):
    print("")
    print(
        color_text.design_text(
            title, color=color, display=disp
        )
    )
    for choice in choices:
        print(color_text.design_text(f"- {choice}", display='bold'))
    print("")


def view_old_label(label):
    print(
        color_text.design_text(
            f"Old label: ", color='red', display='bold'
        ), f"{label}\n"
    )


def run_label_command(imgpath):
    labeler = LabelControl(imgpath)
    labeler.check_file_tracked()

    view_choices(labeler.get_all_labels(), title='Existing labels', disp='negative')
    view_old_label(labeler.get_label())

    label = input("Label: ")

    result = labeler.set_label(label)

    print(result)
