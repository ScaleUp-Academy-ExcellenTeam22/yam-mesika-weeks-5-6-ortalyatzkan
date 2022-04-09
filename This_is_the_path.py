import os
from os import listdir
from os.path import join, isfile
import pathlib


def list_dir_start_with_deep(path:str)->list:
    """
    A function that returns the name of all directory that start with deep in the path he get.
    :param path:Path of Directory.
    :return:All directory that start with deep in the path he get.
    """
    return [file for file in listdir(path) if file.startswith('deep') and os.path.isdir(os.path.join(path, file))]


if __name__== '__main__':
    path_directory = 'C:\\Users\\user\\Desktop\\ortalYatzkan'
    print(list_dir_start_with_deep(path_directory))
