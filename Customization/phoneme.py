"""
Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

# A phoneme, in the context of this application, is an
# object consisting of a name and two file paths, one
# for an image and another for an audio file.
class Phoneme():
    def __init__(self):
        self.name = ""      # name used to refer to the phoneme
        self.text = "" # unique text for describing the sound used
        self.image_path = ""   # full path of the image file
        self.sound_path = ""   # full path of the audio file
        self.image_file = ""   # image filename with extension
        self.sound_file = ""   # audio filename with extension
        self.goal = False            # Whether the phoneme is a goal or not
