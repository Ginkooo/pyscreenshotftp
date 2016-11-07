from pynput.keyboard import Key
from pynput.keyboard import KeyCode

config = {
'ftp_user' : 'ftp', #ftp login, better to be anonymous
'ftp_password' : '', #ftp password
'ftp_host' : '192.168.1.101', #hostname
'folder_local' : 'pics', #a directory, where screenshots are saved locally
'folder_ftp' : 'files', #a directory, where screenshots are saved remotely
'key_combination' : (Key.ctrl, Key.shift, Key.f1), #A combination, wchich triggers the screenshot mechanism. See pynput documentation for full list of possible keys
}
