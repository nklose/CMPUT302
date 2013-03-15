"""
This script loads up the customization interface.

Code for the basic framework was borrowed from:
http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/

Code for using PyQt4 functions is from PyQt Class Reference:
http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys
from PyQt4 import QtCore, QtGui
from gui import Ui_mainWindow
from os.path import basename
from phoneme import *

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Make settings frame invisible until a set is selected
        self.ui.frame.setEnabled(False)

        # Currently selected list elements
        self.currentSet = None
        self.currentPhoneme = None
        self.currentGoal = None

        # Instantiate the set of phoneme sets with a single phoneme
        self.phonemes = [[Phoneme()]]
        self.update_sets()

        #######################################################
        # Interface Object Connections                        #
        #######################################################

        ## List Widgets
        QtCore.QObject.connect(self.ui.listSets,
                               QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),
                               self.select_set)

        QtCore.QObject.connect(self.ui.listPhonemes,
                               QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),
                               self.select_phoneme)

        QtCore.QObject.connect(self.ui.listGoals,
                               QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),
                               self.select_goal)

        ## Buttons

        # Add Set
        QtCore.QObject.connect(self.ui.btnAddSet,
                               QtCore.SIGNAL("clicked()"),
                               self.add_set)

        # Remove Set
        QtCore.QObject.connect(self.ui.btnRemoveSet,
                               QtCore.SIGNAL("clicked()"),
                               self.remove_set)
        
        # Add Phoneme
        QtCore.QObject.connect(self.ui.btnAddPhoneme,
                               QtCore.SIGNAL("clicked()"),
                               self.add_phoneme)

        # Remove Phoneme
        QtCore.QObject.connect(self.ui.btnRemovePhoneme,
                               QtCore.SIGNAL("clicked()"),
                               self.remove_phoneme)

        # Make Goal
        QtCore.QObject.connect(self.ui.btnMakeGoal,
                               QtCore.SIGNAL("clicked()"),
                               self.make_goal)

        # Remove Goal
        QtCore.QObject.connect(self.ui.btnRemoveGoal,
                               QtCore.SIGNAL("clicked()"),
                               self.remove_goal)

        # Load Image
        QtCore.QObject.connect(self.ui.btnLoadImage,
                               QtCore.SIGNAL("clicked()"),
                               self.load_image)

        # Phoneme Sound Buttons
        QtCore.QObject.connect(self.ui.btnA, QtCore.SIGNAL("clicked()"), self.a)
        QtCore.QObject.connect(self.ui.btnO, QtCore.SIGNAL("clicked()"), self.o)
        QtCore.QObject.connect(self.ui.btnEU, QtCore.SIGNAL("clicked()"), self.eu)
        QtCore.QObject.connect(self.ui.btnE_grave, QtCore.SIGNAL("clicked()"), self.e_grave)
        QtCore.QObject.connect(self.ui.btnE_acute, QtCore.SIGNAL("clicked()"), self.e_acute)
        QtCore.QObject.connect(self.ui.btnE, QtCore.SIGNAL("clicked()"), self.e)
        QtCore.QObject.connect(self.ui.btnI, QtCore.SIGNAL("clicked()"), self.i)
        QtCore.QObject.connect(self.ui.btnU, QtCore.SIGNAL("clicked()"), self.u)
        QtCore.QObject.connect(self.ui.btnOU, QtCore.SIGNAL("clicked()"), self.ou)
        QtCore.QObject.connect(self.ui.btnAN, QtCore.SIGNAL("clicked()"), self.an)
        QtCore.QObject.connect(self.ui.btnON, QtCore.SIGNAL("clicked()"), self.on)
        QtCore.QObject.connect(self.ui.btnUN, QtCore.SIGNAL("clicked()"), self.un)
        QtCore.QObject.connect(self.ui.btnIN, QtCore.SIGNAL("clicked()"), self.in2)
        QtCore.QObject.connect(self.ui.btnUI, QtCore.SIGNAL("clicked()"), self.ui2)
        QtCore.QObject.connect(self.ui.btnILL, QtCore.SIGNAL("clicked()"), self.ill)
        QtCore.QObject.connect(self.ui.btnOI, QtCore.SIGNAL("clicked()"), self.oi)
        QtCore.QObject.connect(self.ui.btnP, QtCore.SIGNAL("clicked()"), self.p)
        QtCore.QObject.connect(self.ui.btnB, QtCore.SIGNAL("clicked()"), self.b)
        QtCore.QObject.connect(self.ui.btnF, QtCore.SIGNAL("clicked()"), self.f)
        QtCore.QObject.connect(self.ui.btnV, QtCore.SIGNAL("clicked()"), self.v)
        QtCore.QObject.connect(self.ui.btnM, QtCore.SIGNAL("clicked()"), self.m)
        QtCore.QObject.connect(self.ui.btnR, QtCore.SIGNAL("clicked()"), self.r)
        QtCore.QObject.connect(self.ui.btnT, QtCore.SIGNAL("clicked()"), self.t)
        QtCore.QObject.connect(self.ui.btnD, QtCore.SIGNAL("clicked()"), self.d)
        QtCore.QObject.connect(self.ui.btnS, QtCore.SIGNAL("clicked()"), self.s)
        QtCore.QObject.connect(self.ui.btnZ, QtCore.SIGNAL("clicked()"), self.z)
        QtCore.QObject.connect(self.ui.btnN, QtCore.SIGNAL("clicked()"), self.n)
        QtCore.QObject.connect(self.ui.btnL, QtCore.SIGNAL("clicked()"), self.l)
        QtCore.QObject.connect(self.ui.btnK, QtCore.SIGNAL("clicked()"), self.k)
        QtCore.QObject.connect(self.ui.btnG, QtCore.SIGNAL("clicked()"), self.g)
        QtCore.QObject.connect(self.ui.btnCH, QtCore.SIGNAL("clicked()"), self.ch)
        QtCore.QObject.connect(self.ui.btnJ, QtCore.SIGNAL("clicked()"), self.j)
        QtCore.QObject.connect(self.ui.btnGN, QtCore.SIGNAL("clicked()"), self.gn)

        ## Line Edits
        
        # Add Phoneme Text
        QtCore.QObject.connect(self.ui.txtNewPhoneme,
                               QtCore.SIGNAL("textChanged(const QString&)"),
                               self.check_new_phoneme)

        # Map enter key to button press
        QtCore.QObject.connect(self.ui.txtNewPhoneme,
                               QtCore.SIGNAL("returnPressed()"),
                               self.press_enter)

    # Adds a set to the list of sets
    def add_set(self):
        # Construct set
        newSet = [[]]
        self.phonemes.append(newSet)
        self.update_sets()

    # Removes a set at a given index
    def remove_set(self):
        # delete the item (unless one hasn't been selected yet)
        if self.currentSet != None:
            del self.phonemes[self.currentSet]
            self.update_sets()

            # make frame invisible
            self.ui.frame.setEnabled(False)

    # Updates the displayed list of sets with the internal list.
    def update_sets(self):
        self.ui.listSets.clear()
        index = 1
        for item in self.phonemes:
            self.ui.listSets.addItem("Set " + str(index))
            index += 1
        
        # disable 'remove set' button if there is only one set
        if len(self.phonemes) == 1:
            self.ui.btnRemoveSet.setEnabled(False)
        else:
            self.ui.btnRemoveSet.setEnabled(True)

    # This function is called when the user selects a specific item
    # from the list of sets.
    def select_set(self, set):
        # show frame if it isn't there already
        self.ui.frame.setEnabled(True)

        # get the index of the selected item
        index = self.index_from_set(set)

        # remember index
        self.currentSet = index

        # load phonemes from the current set
        self.update_phonemes()

        # clear current phoneme and current goal
        self.currentPhoneme = None
        self.currentGoal = None

        # disable phoneme-specific ui elements
        self.ui.btnRemovePhoneme.setEnabled(False)
        self.ui.btnMakeGoal.setEnabled(False)
        self.ui.btnRemoveGoal.setEnabled(False)
        self.ui.soundsGroup.setEnabled(False)
        self.ui.btnLoadImage.setEnabled(False)
        self.ui.imgPhoneme.clear()
        
    # Updates the phoneme lists
    def update_phonemes(self):
        # clear displayed lists
        self.ui.listPhonemes.clear()
        self.ui.listGoals.clear()

        # add phonemes into appropriate lists
        for p in range(1, len(self.phonemes[self.currentSet])):
            # get current phoneme
            phoneme = self.phonemes[self.currentSet][p]
            self.ui.listPhonemes.addItem(phoneme.name)
            if phoneme.goal:
                self.ui.listGoals.addItem(phoneme.name)
    
    # This function is called whenever the user selects an items from the phoneme list
    def select_phoneme(self, phoneme):
        # enable 'make goal' button
        self.ui.btnMakeGoal.setEnabled(True)
        
        # enable remove phoneme button
        self.ui.btnRemovePhoneme.setEnabled(True)

        # get the index of the selected item
        index = self.index_from_phoneme(phoneme)

        # remember index
        self.currentPhoneme = index

        # Enable phoneme sounds and load image button
        self.ui.soundsGroup.setEnabled(True)
        self.ui.btnLoadImage.setEnabled(True)

        # Update interface with phoneme information
        phoneme = self.phonemes[self.currentSet][index]
        if phoneme.image_path != "":
            self.ui.lblImagePath = phoneme.image_path
            self.ui.imgPhoneme.setPixmap(QtGui.QPixmap(phoneme.image_path))
        else:
            self.ui.lblImagePath.clear()
            self.ui.imgPhoneme.clear()
        self.select_sound(phoneme.text)

        # Select appropriate sound
        self.select_sound(phoneme.text)
        
    # This function is called whenever the user selects a goal from the goals list,
    def select_goal(self, goal):
        # enable 'remove goal' button
        self.ui.btnRemoveGoal.setEnabled(True)
        
        # get the index of the selected goal
        index = self.index_from_goal(goal)

        # remember index
        self.currentGoal = index

    # This function turns a selected phoneme into a goal phoneme.
    def make_goal(self):
        phoneme = self.phonemes[self.currentSet][self.currentPhoneme]
        phoneme.goal = True
        self.update_phonemes()

    # This function turns a selected goal phoneme into a regular phoneme
    def remove_goal(self):
        goalIndex = self.currentGoal
        
        # make a list of goals
        goals = self.goal_list()

        # set goal to false
        goalPhoneme = goals[goalIndex]
        goalPhoneme.goal = False

        # Disable remove goal button
        self.ui.btnRemoveGoal.setEnabled(False)

        self.update_phonemes()

    # Adds a phoneme to the list of phonemes
    def add_phoneme(self):
        # Construct set
        phoneme = Phoneme()
        
        # set the name for the phoneme
        phoneme.name = str(self.ui.txtNewPhoneme.text())
        self.phonemes[self.currentSet].append(phoneme)
        self.update_phonemes()

        # clear line edit
        self.ui.txtNewPhoneme.clear()

    # Removes a phoneme from the list of phonemes
    def remove_phoneme(self):
        del self.phonemes[self.currentSet][self.currentPhoneme]
        self.update_phonemes()

        # disable phoneme-specific ui elements
        self.ui.btnRemovePhoneme.setEnabled(False)
        self.ui.btnMakeGoal.setEnabled(False)
        self.ui.soundsGroup.setEnabled(False)
        self.ui.btnLoadImage.setEnabled(False)
        self.ui.imgPhoneme.clear()

        # disable remove phoneme button if necessary
        if len(self.phonemes[self.currentSet]) == 0:
            self.ui.btnRemovePhoneme.setEnabled(False)

    # Enables or disables the 'add phoneme' button as necessary
    def check_new_phoneme(self, text):
        # ensure text isn't blank
        if text != "":
            # ensure text is unique
            uniqueName = True
            for p in range(1, len(self.phonemes[self.currentSet])):
                phoneme = self.phonemes[self.currentSet][p]
                if phoneme.name == str(text):
                    uniqueName = False
            if uniqueName:
                self.ui.btnAddPhoneme.setEnabled(True)
            else:
                self.ui.btnAddPhoneme.setEnabled(False)
        else:
            self.ui.btnAddPhoneme.setEnabled(False)

    # Enter key while editing new phoneme text functionality
    def press_enter(self):
        if self.ui.btnAddPhoneme.isEnabled():
            self.add_phoneme()

    # Returns the index of a given set as an integer.
    def index_from_set(self, item):
        return int(item.text()[4:]) - 1
    
    # Returns the index of a given phoneme as an integer.
    def index_from_phoneme(self, item):
        for i in range(0, len(self.phonemes[self.currentSet])):
            phoneme = self.phonemes[self.currentSet][i]
            if str(phoneme.name) == str(item.text()):
                return i
        return None

    # Returns the index of a given goal as an integer.
    def index_from_goal(self, item):
        # count number of goals
        numGoals = self.count_goals()
        
        # make a list of all the goals
        goals = self.goal_list()
            
        # return the index of the selected goal
        for i in range(0, numGoals):
            goal = goals[i]
            if str(item.text()) == str(goal.name):
                return i
        
    # Returns the number of goal phonemes in the selected set
    def count_goals(self):
        goals = 0
        for i in range(0, len(self.phonemes[self.currentSet])):
            phoneme = self.phonemes[self.currentSet][i]
            if phoneme.goal:
                goals += 1
        return goals

    # Makes a list of all goals in the current phoneme set
    def goal_list(self):
        goals = []
        for i in range(0, len(self.phonemes[self.currentSet])):
            phoneme = self.phonemes[self.currentSet][i]
            if phoneme.goal:
                goals.append(phoneme)
        return goals

    # Loads an image into the interface and saves it into the phoneme object
    def load_image(self):
        phoneme = self.phonemes[self.currentSet][self.currentPhoneme]
        phoneme.image_path = str(QtGui.QFileDialog.getOpenFileName())
        phoneme.image_file = basename(phoneme.image_path)

        self.ui.imgPhoneme.setPixmap(QtGui.QPixmap(phoneme.image_path))
        self.ui.lblImagePath.setText(phoneme.image_file)

    # Individual phoneme sound button functions
    def a(self):
        self.select_sound("a")
    def o(self):
        self.select_sound("o")
    def eu(self):
        self.select_sound("eu")
    def e_grave(self):
        self.select_sound("e_grave")
    def e_acute(self):
        self.select_sound("e_acute")
    def e(self):
        self.select_sound("e")
    def i(self):
        self.select_sound("i")
    def u(self):
        self.select_sound("u")
    def ou(self):
        self.select_sound("ou")
    def an(self):
        self.select_sound("an")
    def on(self):
        self.select_sound("on")
    def un(self):
        self.select_sound("un")
    def in2(self):
        self.select_sound("in")
    def ui2(self):
        self.select_sound("ui")
    def ill(self):
        self.select_sound("ill")
    def oi(self):
        self.select_sound("oi")
    def p(self):
        self.select_sound("p")
    def b(self):
        self.select_sound("b")
    def f(self):
        self.select_sound("f")
    def v(self):
        self.select_sound("v")
    def m(self):
        self.select_sound("m")
    def r(self):
        self.select_sound("r")
    def t(self):
        self.select_sound("t")
    def d(self):
        self.select_sound("d")
    def s(self):
        self.select_sound("s")
    def z(self):
        self.select_sound("z")
    def n(self):
        self.select_sound("n")
    def l(self):
        self.select_sound("l")
    def k(self):
        self.select_sound("k")
    def g(self):
        self.select_sound("g")
    def ch(self):
        self.select_sound("ch")
    def j(self):
        self.select_sound("j")
    def gn(self):
        self.select_sound("gn")

    # Selects a specific sound button
    def select_sound(self, s):
        self.deselect_all()
        if s == "a":
            self.ui.btnA.setChecked(True)
        elif s == "o":
            self.ui.btnO.setChecked(True)
        elif s == "eu":
            self.ui.btnEU.setChecked(True)
        elif s == "e_grave":
            self.ui.btnE_grave.setChecked(True)
        elif s == "e_acute":
            self.ui.btnE_acute.setChecked(True)
        elif s == "i":
            self.ui.btnI.setChecked(True)
        elif s == "u":
            self.ui.btnU.setChecked(True)
        elif s == "ou":
            self.ui.btnOU.setChecked(True)
        elif s == "an":
            self.ui.btnAN.setChecked(True)
        elif s == "on":
            self.ui.btnON.setChecked(True)
        elif s == "un":
            self.ui.btnUN.setChecked(True)
        elif s == "in":
            self.ui.btnIN.setChecked(True)
        elif s == "ui":
            self.ui.btnUI.setChecked(True)
        elif s == "ill" or s == "y":
            self.ui.btnILL.setChecked(True)
        elif s == "oi" or s == "w":
            self.ui.btnOI.setChecked(True)
        elif s == "p":
            self.ui.btnP.setChecked(True)
        elif s == "b":
            self.ui.btnB.setChecked(True)
        elif s == "f":
            self.ui.btnF.setChecked(True)
        elif s == "v":
            self.ui.btnV.setChecked(True)
        elif s == "m":
            self.ui.btnM.setChecked(True)
        elif s == "r":
            self.ui.btnR.setChecked(True)
        elif s == "t":
            self.ui.btnT.setChecked(True)
        elif s == "d":
            self.ui.btnD.setChecked(True)
        elif s == "s":
            self.ui.btnS.setChecked(True)
        elif s == "z":
            self.ui.btnZ.setChecked(True)
        elif s == "n":
            self.ui.btnN.setChecked(True)
        elif s == "l":
            self.ui.btnL.setChecked(True)
        elif s == "k":
            self.ui.btnK.setChecked(True)
        elif s == "g":
            self.ui.btnG.setChecked(True)
        elif s == "ch":
            self.ui.btnCH.setChecked(True)
        elif s == "j":
            self.ui.btnJ.setChecked(True)
        elif s == "gn":
            self.ui.btnGN.setChecked(True)

        # update current phoneme sound
        if s != "":
            phoneme = self.phonemes[self.currentSet][self.currentPhoneme]
            phoneme.text = s

    # Deselects all sound buttons in the phoneme sounds section
    def deselect_all(self):
        self.ui.btnA.setChecked(False)
        self.ui.btnO.setChecked(False)
        self.ui.btnEU.setChecked(False)
        self.ui.btnE_grave.setChecked(False)
        self.ui.btnE_acute.setChecked(False)
        self.ui.btnE.setChecked(False)
        self.ui.btnI.setChecked(False)
        self.ui.btnU.setChecked(False)
        self.ui.btnOU.setChecked(False)
        self.ui.btnAN.setChecked(False)
        self.ui.btnON.setChecked(False)
        self.ui.btnUN.setChecked(False)
        self.ui.btnIN.setChecked(False)
        self.ui.btnUI.setChecked(False)
        self.ui.btnILL.setChecked(False)
        self.ui.btnOI.setChecked(False)
        self.ui.btnP.setChecked(False)
        self.ui.btnB.setChecked(False)
        self.ui.btnF.setChecked(False)
        self.ui.btnV.setChecked(False)
        self.ui.btnM.setChecked(False)
        self.ui.btnR.setChecked(False)
        self.ui.btnT.setChecked(False)
        self.ui.btnD.setChecked(False)
        self.ui.btnS.setChecked(False)
        self.ui.btnZ.setChecked(False)
        self.ui.btnN.setChecked(False)
        self.ui.btnL.setChecked(False)
        self.ui.btnK.setChecked(False)
        self.ui.btnG.setChecked(False)
        self.ui.btnCH.setChecked(False)
        self.ui.btnJ.setChecked(False)
        self.ui.btnGN.setChecked(False)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
