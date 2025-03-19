from imgFolder.controllers import (
    LabelControl,
    IndexControl
)
from imgFolder.utils import color_text


def view_list(case_list: list, title, title_color='cyan', title_disp='bold'):
    print("")
    print(
        color_text.design_text(
            title, color=title_color, display=title_disp
        )
    )
    for case in case_list:
        print(color_text.design_text(f"- {case}", display='bold'))
    print("")    


def view_pairs(case_list: list[tuple], title, title_color='cyan', title_disp='bold'):
    print("")
    print(
        color_text.design_text(
            title, color=title_color, display=title_disp
        )
    )
    for case in case_list:
        print(color_text.design_text(f"{case[0]} - {case[1]}", display='bold'))
    print("") 


def view_old_label(label):
    print(
        color_text.design_text(
            f"Old label: ", color='red', display='bold'
        ), f"{label}\n"
    )


def run_label_image_command(imgpath):
    labeler = LabelControl(imgpath)
    labeler.check_file_tracked()

    view_list(labeler.get_all_labels(), title='Existing labels', disp='negative')
    view_old_label(labeler.get_label())

    label = input("Label: ")

    labeler.set_label(label)

    print({imgpath:labeler.get_label()})


def run_track_folder_command():
    index = IndexControl()
    try:
        index.start_tracking_folder()
    except Exception as e:
        print("This folder's images are already being tracked.")


def run_show_labels_command(with_images=False):
    labeler = LabelControl(imgpath=None)
    if not with_images:
        all_labels = labeler.get_all_labels()
        view_list(all_labels, title='Existing labels')

    else:
        img_labels = labeler.get_imgs_and_labels()
        view_pairs(img_labels, title="Labels and images")