import os


def make_filename():
    import datetime
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    timestamp_without_dot = str(timestamp).replace(".", "")
    filename = timestamp_without_dot + '.jpg'
    return filename

def copy_to_clipboard(filename):
    os.popen('echo {filename} | xclip -selection clipboard'.format(filename = filename))

def play_sound():
    pass
