# pyscreenshotftp
A small program in Python, allowing to take screenshot of a selected part of the screen, upload it to FTP server and copy a link to it, so it could be parted and sent on Facebook etc.

This program needs xcopy and ImageMagick installed and accessible from terminal
to work, beside pip requirements in requirements.txt file.

You have to have ftp server connected for this to work (Anonymous access is
preffered, but not necessary)

How to install dependencies:

1. Install Python 3 from your package manager or home site.
2. Install pip for python 3.
3. Run pip install -r /path/to/requirements.txt (change it to relative path to
   your requirements.txt)
4. Install ImageMagick and xclip



- Look to file config.py if you want to configure your settings.

Run main.py with python to run the program
