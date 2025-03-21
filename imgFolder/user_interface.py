import argparse

from imgFolder.commands import (
    run_label_image_command,
    run_track_folder_command,
    run_show_labels_command
)

def main(options):
    if options.command == "label_image":
        run_label_image_command(options.img_path)
    if options.command == "init_folder":
        run_track_folder_command()
    if options.command == "show_labels":
        run_show_labels_command(options.with_images)


def set_commands():
    main_parser = argparse.ArgumentParser(
        prog='imgFolder',
        description=("CLI used for running a suite of tools to help "
                     "manage an Image folder.")
    )

    subparsers = main_parser.add_subparsers(
        help="Available tools.",
        dest="command"
    )

    parse_label_image(subparsers)
    parse_track_folder(subparsers)
    parse_show_labels(subparsers)

    return main_parser



def parse_label_image(parsers):
    label_parser = parsers.add_parser(
        name="label_image", 
        help="Give a chosen tag to a specified image."
    )

    label_parser.add_argument(
        'img_path', 
        type=str, 
        help='Path of the image to be labeled.'
    )


def parse_track_folder(parsers):
    track_parser = parsers.add_parser(
        name="init_folder", 
        help="Start tracking the images from the folder to manage."
    )


def parse_show_labels(parsers):
    show_label_parser = parsers.add_parser(
        name="show_labels", 
        help="Show all images tracked and their corresponding labels."
    )

    show_label_parser.add_argument(
        '--with_images', 
        action='store_true',
        help='Path of the image to be labeled.'
    )