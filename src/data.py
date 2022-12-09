#---------------------------------------------
from param import param_hu

import os


def check_directories():
    create_directory(param_hu.path_data_dir)
    create_directory(param_hu.path_image_dir)
    create_or_clear_dir(param_hu.path_frame_dir)
    create_or_clear_dir(param_hu.path_predi_dir)
    set_image_empty()

def create_or_clear_dir(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mOK\033[0m] Directory \033[96m%s\033[0m created" % path)
    else:
        for file in os.scandir(path):
            os.remove(file.path)

def create_directory(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mOK\033[0m] Directory \033[96m%s\033[0m created" % path)

def set_image_empty():
    command = "cp " + param_hu.path_generic + "image_empty " + param_hu.path_image_dir + "/image"
    os.system(command)
