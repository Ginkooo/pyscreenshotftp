from ftplib import FTP
from config import config
import os

ftp = FTP(host=config.get('ftp_host'), user=config.get('ftp_user'), passwd=config.get('ftp_password'))

def upload_file(filepath):
    """Function, which uploads one file to a configured ftp server

    Args:
    string : filepath - a path to file to send

    Returns:
    string: link - a link to uploaded file, with ftp:// prefix"""

    path_to_file_folder = os.path.dirname(filepath)
    os.chdir(path_to_file_folder)
    filename = os.path.basename(filepath)

    folder = config.get('folder_ftp')

    while not os.path.exists(filename):
        pass

    ftp.storbinary("STOR {folder}/{filename}".format(filename = filename, folder = folder), open(filename, "rb"))

    link = '{host}/{folder}/{filename}'.format(host = config.get('ftp_host'), filename = filename, folder = folder)
    return link
