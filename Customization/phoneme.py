"""
Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

# A phoneme, in the context of this application, is an
# object consisting of a name and two file paths, one
# for an image and another for an audio file.
class Phoneme():
    def __init__(self):
        self.name = ""         # name used to refer to the phoneme
        self.text = ""         # unique text for describing the sound used
        self.image_path = ""   # full path of the image file
        self.sound_path = ""   # full path of the audio file
        self.goal = False      # Whether the phoneme is a goal or not

    # Returns the phoneme information as a string
    def toString(self):
        string = "\t[name = " + self.name + "\n\ttext = " + self.text
        string += "\n\timage_path = " + self.image_path + "\n\tsound_path = "
        string += self.sound_path + "\n\tgoal = " + str(self.goal) + "]"
        return string

# A set consists of a list of phonemes, from which a few are selected
# during a playthrough.
class Set():
    def __init__(self):
        self.phonemes = []

    # Clears all phonemes from the set
    def clear(self):
        self.phonemes = []

    # Adds a new phoneme to the set
    def add_phoneme(self, phoneme=None):
        if phoneme == None:
            phoneme = Phoneme()
        self.phonemes.append(phoneme)

    # Removes a phoneme at a given index from the set
    def remove_phoneme(self, index):
        del self.phonemes[index]

    # Marks all phonemes in the set as non-goals
    def clear_goals(self):
        for phoneme in self.phonemes:
            phoneme.goal = False

    # Sets a phoneme at a given index as the goal for the set
    def set_goal_index(self, index):
        self.clear_goals()
        goalPhoneme = self.phonemes[index]
        goalPhoneme.goal = True

    # Returns the list of phonemes in the set as a string
    def toString(self):
        string = "["
        for item in self.phonemes:
            string += item.name
            string += ", "
        if len(string) > 2:
            string = string[:-2]
        string += "]"
        return string

# A level consists of a list of sets.
class Level():
    def __init__(self):
        self.sets = []

    # Clears all sets from the level
    def clear(self):
        self.sets = []

    # Adds a new set to the level
    def add_set(self, set=None):
        if set == None:
            set = Set()
        self.sets.append(set)

    # Removes a set at a given index from the level
    def remove_set(self, index):
        del self.sets[index]
    
# A game consists of a list of levels as well as variables for each difficulty slider.
class Game():
    def __init__(self):
        self.levels = []
        self.failedAttemptsWeight = 50
        self.hintsRequestedWeight = 50
        self.timeWeight = 50
