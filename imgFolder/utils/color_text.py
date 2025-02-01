from functools import partial

def color_text(text, num):
    return f"\033[0;{num}m{text}\033[0m"

def display_text(text, num):
    return f"\033[{num}m{text}\033[0m"

DISPLAY_FUNC = {
    "bold"            : partial(display_text, num=1),
    "italic"          : partial(display_text, num=3),
    "underline"       : partial(display_text, num=4),
    "negative"        : partial(display_text, num=7),
    "striked"         : partial(display_text, num=9),
    "double_underline": partial(display_text, num=21),
}

FG_COLOR_FUNC = {
    "black"  : partial(color_text, num=30),
    "red"    : partial(color_text, num=31),
    "green"  : partial(color_text, num=32),
    "yellow" : partial(color_text, num=33),
    "blue"   : partial(color_text, num=34),
    "magenta": partial(color_text, num=35),
    "cyan"   : partial(color_text, num=36),
    "white"  : partial(color_text, num=37)
}

def neutral(text):
    return text

def design_text(text, color=None, display=None):
    """
    Set a format for the text to be displayed on the terminal.
    Color controls the text color, and display controls the
    font rendition.

    Parameters:
    -----------
    color: str
        Can be any of the following
        black, red, green, yellow, blue, magenta,
        cyan, white

    display: str
        Can be any of the following

    """
    display_func = DISPLAY_FUNC.get(display, neutral)
    color_func = FG_COLOR_FUNC.get(color, neutral)

    return color_func(display_func(text))