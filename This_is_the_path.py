import os
from os import listdir
from os.path import join, isfile
import pathlib

#a function that returns the name of all directory that start with deep in the path he get
def list_dir_start_with_deep(path):
     return [ file for file in listdir(path) if file.startswith('deep') and os.path.isdir(os.path.join(path, file))]



if __name__== '__main__':
    path = 'C:\\Users\\user\\Desktop\\ortalYatzkan'
    print(list_dir_start_with_deep(path))