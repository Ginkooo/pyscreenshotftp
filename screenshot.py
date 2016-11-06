import os
import tools
from config import config


def do_a_ss_and_return_path(upper_corner_coords, width_of_ss, height_of_ss):
    curr_path = os.getcwd()

    folder = config.get('folder_local')

    filename = tools.make_filename()

    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, filename)

    os.popen("""convert x:'root[{x}x{y}+{offset_x}+{offset_y}]' {path}""".format(x = width_of_ss, y = height_of_ss,\
                                                                    offset_x = upper_corner_coords[0], offset_y = upper_corner_coords[1], path = path))

    return path
