# A phoneme set is an arbitrarily long list of phonemes.
# One phoneme is the goal, and the rest are distractors.
# Each phoneme set must have a goal.
class Phoneme_Set():
    def __init__(self):
        self.goal = Phoneme()
        self.distractors = []

# A phoneme, in the context of this application, is an
# object consisting of a name and two file paths, one
# for an image and another for an audio file.
class Phoneme():
    def __init__(self):
        self.name = "<Unnamed>"
        self.image_path = "<none>"
        self.sound_path = "<none>"
        self.image_file = "<none>"
        self.sound_file = "<none>"
