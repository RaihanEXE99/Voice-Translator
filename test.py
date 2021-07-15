import os
from os.path import join,isfile
# from string import join

path="temp_files"

first_file = next(join(path, f) for f in os.listdir(path) if isfile(join(path, f)))

print(first_file)