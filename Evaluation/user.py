"""
This file defines classes needed for evaluation.py.

Code for the basic framework was borrowed from:
http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/

Code for using PyQt4 functions is from PyQt Class Reference:
http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

# A user has a group of statistics, which consists of various ResultGroups.
# There is one for the totals, one for the averages, and ten for the levels.
class User():
    def __init__(self, name = None):
        self.name = None
        if name == None:
            self.name = "Default"
        else:
            self.name = name
        self.total = ResultGroup()
        self.average = ResultGroup()
        self.level = []
        for i in range(0, 10):
            self.level.append(ResultGroup())

# A ResultGroup is a group of evaluation results containing the number of 
# hints, attempts, and seconds (time) for a particular game component.
class ResultGroup():
    def __init__(self):
        self.hints = 0
        self.attempts = 0
        self.time = 0
