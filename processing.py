import os,glob
from os.path import join,isfile
from subprocess import check_output

def generateOutput(file_path,language,ext):
    # print(["autosub","-i",file_path,"-S",language,"-F",ext])
    path="temp_files"
    out = check_output(["autosub","-i",file_path,"-S",language,"-F",ext])
    os.remove(file_path)
    first_file = next(join(path, f) for f in os.listdir(path) if isfile(join(path, f)))
    f = open(first_file, "r")
    print(f.read(),type(f.read()))
    # print(out)
    # return "exit"
    return out