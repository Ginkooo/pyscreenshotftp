import os


def make_filename():
    """It makes filename of a jpg depending on a current time

    Returns:
    string : filename - name made of a timestamp"""

    import datetime
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    timestamp_without_dot = str(timestamp).replace(".", "")
    filename = timestamp_without_dot + '.jpg'
    return filename

def copy_to_clipboard(filename):
    """A function which copies a string to a clipboard using xclip program

    Args:
    string: filename - a given string to copy"""
    os.popen('echo {filename} | xclip -selection clipboard'.format(filename = filename))

def play_sound():
    """Not implemented yet, desired to play some sound when part of the screen is selected correctly"""
    pass
