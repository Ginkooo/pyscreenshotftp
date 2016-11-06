def make_filename():
    import datetime
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    timestamp_without_dot = str(timestamp).replace(".", "")
    filename = timestamp_without_dot + '.jpg'
    return filename
