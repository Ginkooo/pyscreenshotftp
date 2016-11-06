from tools import make_filename
from ftplib import FTP
from config import config
import os
from ftp import upload_file

def test_ftp_stor():
    ftp = FTP(host=config.get('ftp_host'), user=config.get('ftp_user'), passwd=config.get('ftp_password'))
    f = open("file", "w")
    f.write("AEZAKMI")
    f.close()
    ftp.storbinary("STOR file", open("file", "rb"))
    os.remove("file")

def test_ftp_init():
    ftp = FTP(host=config.get('ftp_host'), user=config.get('ftp_user'), passwd=config.get('ftp_password'))
    ftp.retrlines('LIST')

def test_long_filenames():
    ftp = FTP(host=config.get('ftp_host'), user=config.get('ftp_user'), passwd=config.get('ftp_password'))
    f = open("1231242332435345.jpg", "w")
    f.write("AEZAKMI")
    f.close()
    ftp.storbinary("STOR files/1231242332435345.jpg", open("1231242332435345.jpg", "rb"))
    os.remove("file")



def test_upload():
    f = open("file", "w")
    f.write("Sample text")
    f.close()
    upload_file("./file")
#test_ftp_stor()
test_long_filenames()

test_ftp_init()
