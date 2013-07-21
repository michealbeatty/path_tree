#! /usr/bin/env python3
''' This program will generate a list of all subdirectories
and files within the current working directory'''

import os

# Grab current directory and create a file name based upon that.

currentdirectory = os.getcwd()
dirname = currentdirectory.split('/')
pathfile = dirname[-1] + ".path"

f = open(pathfile, 'a')

#walk the directory and write the results to a file
for dirname, dirnames, filenames in os.walk(currentdirectory):
    
    # print path to all subdirectories first.
    for subdirname in dirnames:
        f.write(os.path.join(dirname, subdirname) + "\n")

    # print path to all filenames.
    for filename in filenames:
        f.write(os.path.join(dirname, filename) + "\n")
f.close()