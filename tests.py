from tools import make_filename
from ftplib import FTP
from config import config
import os
from ftp import upload_file

from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput.keyboard import KeyCode
from pynput.mouse import Controller

keys = (Key.ctrl, Key.shift, Key.f1)
pressed = [False for x in keys]

def on_press(key):
    print('{key} pressed'.format(key = key))
    if key in keys:
        idx = keys.index(key)
        pressed[idx] = True
    if key == Key.esc:
        return False


def on_release(key):
    all_pressed = True
    for val in pressed:
        if not val:
            all_pressed = False
    if all_pressed:
        print("All keys pressed")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

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
