"""
This script changes the saved file system from images saved
within word documents to a file system with folders and images

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys, os, shutil, ntpath

print ("Simple Script to reverse the changes made by Photo Exctration")

path = os.getcwd()

def undoExtraction():
    for root,d,f in os.walk(path):
        for files in f:
            if files.endswith(".docx"):
                shutil.move(os.path.join(root, files), os.path.join(root, "..") )
                shutil.rmtree(root)

undoExtraction()
