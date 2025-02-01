import argparse

from imgFolder.commands import (
    run_label_command
)

def main(options):
    if options.command == "label_image":
        run_label_command(options.img_path)



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

    label_parser = subparsers.add_parser(
        name="label_image", 
        help="Give a chosen tag to a specified image."
    )

    label_parser.add_argument(
        'img_path', 
        type=str, 
        help='Path of the image to be labeled.'
    )

    return main_parser
