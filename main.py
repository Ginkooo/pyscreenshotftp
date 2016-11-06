import screenshot
import keygetter
import os
import tools
import ftp
import paste

while True:
    ss_bounds = keygetter.triggered()

    if not len(ss_bounds):
        break;

    start = ss_bounds[0]
    end = ss_bounds[1]

    width_of_ss = abs(end[0] - start[0])
    height_of_ss = abs(end[1] - start[1])

    upper_corner_coords = []

    if start[0] < end[0]:
        upper_corner_coords.append(start[0])
    else:
        upper_corner_coords.append(end[0])

    if start[1] < end[1]:
        upper_corner_coords.append(start[1])
    else:
        upper_corner_coords.append(end[1])


    path = screenshot.do_a_ss_and_return_path(upper_corner_coords, width_of_ss, height_of_ss)


    filelink = '{prefix}{link}'.format(prefix = 'ftp://', link = ftp.upload_file(path))

    print (filelink)

    tools.copy_to_clipboard(filelink)
