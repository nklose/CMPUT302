"""
This script loads up the customization interface.

Code for the basic framework was borrowed from:
http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/

Code for using PyQt4 functions is from PyQt Class Reference:
http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys, os
import pickle
from PyQt4 import QtCore, QtGui
from gui import Ui_mainWindow
from os.path import basename
from phoneme import *
from sounds import Phoneme_Sound
from sounds import Sounds
from sounds import Ui_Dialog
from datetime import datetime
from file_customizer import compile_elf, generate_files

# Constant globals
NUM_LEVELS = 10
DEBUG = False # print debug info to console
if len(sys.argv) > 1:
    if sys.argv[1] == "debug": # check for command-line argument
        DEBUG = False

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Make settings frame invisible until a set is selected
        self.ui.frame.setEnabled(False)
        self.msg("Enabling frame.")

        # Clear lists
        self.ui.listSets.clear()
        self.ui.listPhonemes.clear()

        # Indices of objects currently selected in the interface
        self.levelIndex = 0
        self.setIndex = None
        self.phonemeIndex = None

        # Instantiate all levels
        self.levels = []
        for n in range(0, NUM_LEVELS):
            self.levels.append(Level())
            self.msg("Adding level " + str(n+1))
            
        # Update the displayed list of sets
        self.update_sets()
        self.msg("Updating set list.")

        #######################################################
        # Interface Object Connections                        #
        #######################################################
        itemClicked = QtCore.SIGNAL("itemClicked(QListWidgetItem *)")
        clicked = QtCore.SIGNAL("clicked()")

        ## List Widgets
        QtCore.QObject.connect(self.ui.listSets, itemClicked, self.select_set)
        QtCore.QObject.connect(self.ui.listPhonemes,itemClicked, self.select_phoneme)

        ## Buttons
        QtCore.QObject.connect(self.ui.btnAddSet, clicked, self.add_set)
        QtCore.QObject.connect(self.ui.btnRemoveSet, clicked, self.remove_set)
        QtCore.QObject.connect(self.ui.btnAddPhoneme, clicked, self.add_phoneme)
        QtCore.QObject.connect(self.ui.btnRemovePhoneme, clicked, self.remove_phoneme)
        QtCore.QObject.connect(self.ui.btnSetGoal, clicked, self.set_goal)
        QtCore.QObject.connect(self.ui.btnLoadImage, clicked, self.load_image)
        QtCore.QObject.connect(self.ui.btnModifySounds, clicked, self.modify_sounds)
        QtCore.QObject.connect(self.ui.btnSave, clicked, self.save)
        QtCore.QObject.connect(self.ui.btnLoad, clicked, self.load)
        QtCore.QObject.connect(self.ui.btnInstall, clicked, self.install)
        QtCore.QObject.connect(self.ui.btnCustom, clicked, self.custom_sound)

        QtCore.QObject.connect(self.ui.btnA, clicked, self.a)
        QtCore.QObject.connect(self.ui.btnO, clicked, self.o)
        QtCore.QObject.connect(self.ui.btnEU, clicked, self.eu)
        QtCore.QObject.connect(self.ui.btnE_grave, clicked, self.e_grave)
        QtCore.QObject.connect(self.ui.btnE_acute, clicked, self.e_acute)
        QtCore.QObject.connect(self.ui.btnE, clicked, self.e)
        QtCore.QObject.connect(self.ui.btnI, clicked, self.i)
        QtCore.QObject.connect(self.ui.btnU, clicked, self.u)
        QtCore.QObject.connect(self.ui.btnOU, clicked, self.ou)
        QtCore.QObject.connect(self.ui.btnAN, clicked, self.an)
        QtCore.QObject.connect(self.ui.btnON, clicked, self.on)
        QtCore.QObject.connect(self.ui.btnUN, clicked, self.un)
        QtCore.QObject.connect(self.ui.btnIN, clicked, self.in2)
        QtCore.QObject.connect(self.ui.btnUI, clicked, self.ui2)
        QtCore.QObject.connect(self.ui.btnILL, clicked, self.ill)
        QtCore.QObject.connect(self.ui.btnOI, clicked, self.oi)
        QtCore.QObject.connect(self.ui.btnP, clicked, self.p)
        QtCore.QObject.connect(self.ui.btnB, clicked, self.b)
        QtCore.QObject.connect(self.ui.btnF, clicked, self.f)
        QtCore.QObject.connect(self.ui.btnV, clicked, self.v)
        QtCore.QObject.connect(self.ui.btnM, clicked, self.m)
        QtCore.QObject.connect(self.ui.btnR, clicked, self.r)
        QtCore.QObject.connect(self.ui.btnT, clicked, self.t)
        QtCore.QObject.connect(self.ui.btnD, clicked, self.d)
        QtCore.QObject.connect(self.ui.btnS, clicked, self.s)
        QtCore.QObject.connect(self.ui.btnZ, clicked, self.z)
        QtCore.QObject.connect(self.ui.btnN, clicked, self.n)
        QtCore.QObject.connect(self.ui.btnL, clicked, self.l)
        QtCore.QObject.connect(self.ui.btnK, clicked, self.k)
        QtCore.QObject.connect(self.ui.btnG, clicked, self.g)
        QtCore.QObject.connect(self.ui.btnCH, clicked, self.ch)
        QtCore.QObject.connect(self.ui.btnJ, clicked, self.j)
        QtCore.QObject.connect(self.ui.btnGN, clicked, self.gn)

        ## Others
        QtCore.QObject.connect(self.ui.txtNewPhoneme,
                               QtCore.SIGNAL("textChanged(const QString&)"),
                               self.check_new_phoneme)
        QtCore.QObject.connect(self.ui.txtNewPhoneme,
                               QtCore.SIGNAL("returnPressed()"),
                               self.press_enter)
        QtCore.QObject.connect(self.ui.verticalSlider,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.change_level)


    # Updates the displayed list of sets with the internal list.
    def update_sets(self):
        # get the list of sets in the selected level
        level = self.get_level()
        levelSets = level.sets

        # clear the displayed sets
        self.ui.listSets.clear()
        self.msg("Clearing set list.")

        # add each set to the list
        index = 1
        for item in levelSets:
            self.ui.listSets.addItem("Set " + str(index))
            self.msg("Adding set index " + str(index))
            index += 1
        
        # disable 'remove set' button if necessary
        if len(levelSets) < 2:
            self.ui.btnRemoveSet.setEnabled(False)
            self.msg("Disabling remove set button. (sets = " + str(len(levelSets)) + ")")
        else:
            self.ui.btnRemoveSet.setEnabled(True)
            self.msg("Enabling remove set button. (sets = " + str(len(levelSets)) + ")")

    # This function is called when the user selects a set from the list
    def select_set(self, item):
        # show frame if it isn't there already
        self.ui.frame.setEnabled(True)

        # get the index of the selected item
        index = self.set_index(item)

        # remember index
        self.setIndex = index

        # load phonemes from the current set
        self.update_phonemes()

        # clear current phoneme and current goal
        self.phonemeIndex = None

        # disable phoneme-specific ui elements
        self.reset_phoneme_ui()

        # debug string
        currentSet = self.get_set()
        string = "Selecting set at index " + str(index) + ":" 
        string += currentSet.toString()
        self.msg(string)

    # This function removes phoneme-specific content from the UI
    def reset_phoneme_ui(self):
        self.ui.btnRemovePhoneme.setEnabled(False)
        self.ui.btnSetGoal.setEnabled(False)
        self.ui.soundsGroup.setEnabled(False)
        self.ui.imageGroup.setEnabled(False)
        self.ui.lblSoundPath.clear()
        self.ui.lblImagePath = ""
        self.ui.imgPhoneme.clear()
        
    # Enables phoneme-specific content in the UI
    def enable_phoneme_ui(self):
        self.ui.btnRemovePhoneme.setEnabled(True)
        self.ui.btnSetGoal.setEnabled(True)
        self.ui.soundsGroup.setEnabled(True)
        self.ui.imageGroup.setEnabled(True)

    # Updates the phoneme lists
    def update_phonemes(self):
        # clear phoneme list
        self.ui.listPhonemes.clear()

        # add phonemes into appropriate lists
        phonemes = self.get_set().phonemes
        if phonemes != None:
            for p in range(0, len(phonemes)):
                # get current phoneme
                phoneme = phonemes[p]
                if phoneme.goal:
                    self.ui.listPhonemes.addItem(phoneme.name + " (GOAL)")
                else:
                    self.ui.listPhonemes.addItem(phoneme.name)
    
    # This function is called whenever the user selects an items from the phoneme list
    def select_phoneme(self, phoneme):
        # enable 'make goal' button
        self.enable_phoneme_ui()

        # get the index of the selected item
        index = self.phoneme_index(phoneme)

        # remember index
        self.phonemeIndex = index

        # Enable phoneme sounds and load image button
        self.ui.soundsGroup.setEnabled(True)
        self.ui.btnLoadImage.setEnabled(True)

        self.ui.lblSoundPath.clear()

        # Update interface with phoneme information
        p = self.get_phoneme()
        self.msg("Index: " + str(index))
        self.msg("Selected phoneme at index " + str(index) + ":\n" + p.toString())
        if p.image_path != "":
            self.ui.lblImagePath = p.image_path
            self.ui.imgPhoneme.setPixmap(QtGui.QPixmap(p.image_path))
        else:
            self.ui.lblImagePath = ""
            self.ui.imgPhoneme.clear()
        self.select_sound(p.text)

        # Select appropriate sound
        self.select_sound(p.text)

    # Enables or disables the 'add phoneme' button as necessary
    def check_new_phoneme(self, text):
        # ensure text isn't blank
        if text != "":
            # ensure text is unique
            uniqueName = True
            currentSet = self.get_set()
            phonemes = currentSet.phonemes
            if phonemes != None:
                for p in range(0, len(phonemes)):
                    phoneme = phonemes[p]
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

    # Loads an image into the interface and saves it into the phoneme object
    def load_image(self):
        phoneme = self.get_phoneme()
        phoneme.image_path = str(QtGui.QFileDialog.getOpenFileName())
        phoneme.image_file = basename(phoneme.image_path)

        self.ui.imgPhoneme.setPixmap(QtGui.QPixmap(phoneme.image_path))
        self.ui.lblImagePath = phoneme.image_file

    # Returns the currently selected level
    def get_level(self):
        return self.levels[self.levelIndex]

    # Returns the currently selected set
    def get_set(self):
        level = self.levels[self.levelIndex]
        if self.setIndex != None:
            return level.sets[self.setIndex]
        else:
            return None

    # Returns the currently selected phoneme
    def get_phoneme(self):
        set = self.get_set()
        if self.phonemeIndex != None:
            return set.phonemes[self.phonemeIndex]
        else:
            return None
        
    # Returns the index of a given set as an integer.
    def set_index(self, item):
        return int(item.text()[4:]) - 1 # get text from set string
    
    # Returns the index of a given phoneme as an integer.
    def phoneme_index(self, item):
        currentSet = self.get_set()
        phonemes = currentSet.phonemes
        for i in range(0, len(phonemes)):
            phoneme = phonemes[i]
            self.msg("Phoneme name: " + str(phoneme.name))
            self.msg("Item text: " + str(item.text()))
            self.msg("Item text [:-7]: " + str(item.text())[:-7])
            if str(phoneme.name) == str(item.text()):
                self.msg("Item text == phoneme name")
                return i
            elif str(phoneme.name) == str(item.text())[:-7]:
                self.msg("Item text + goal == phoneme name")
                return i
        return None

    # Adds a set to the currently selected level
    def add_set(self):
        level = self.get_level()
        self.msg("Adding set.")
        level.add_set()
        self.update_sets()

    # Removes a set from the currently selected level
    def remove_set(self):
        if self.setIndex != None:
            level = self.get_level()
            self.msg("Removing set at index " + str(self.setIndex))
            level.remove_set(self.setIndex)
            self.update_sets()

    # Adds a phoneme to the currently selected set
    def add_phoneme(self):
        # build phoneme
        phoneme = Phoneme()
        phoneme.name = str(self.ui.txtNewPhoneme.text())

        # clear input text
        self.ui.txtNewPhoneme.clear()

        # add phoneme to set
        currentSet = self.get_set()
        self.msg("Adding phoneme " + phoneme.name)
        currentSet.add_phoneme(phoneme)
        self.msg("Current set: " + currentSet.toString())

        # update phoneme list
        self.update_phonemes()

    # Removes a phoneme from the currently selected set
    def remove_phoneme(self):
        if self.phonemeIndex != None:
            currentSet = self.get_set()
            self.msg("Removing phoneme at index " + str(self.phonemeIndex))
            currentSet.remove_phoneme(self.phonemeIndex)
            self.reset_phoneme_ui()
            self.update_phonemes()

    # Sets the currently selected phoneme as the goal for the set
    def set_goal(self):
        if self.phonemeIndex != None:
            currentSet = self.get_set()
            currentSet.set_goal_index(self.phonemeIndex)
            self.update_phonemes()

    # Loads the phoneme sound modification inderface
    def modify_sounds(self):
        # load up sounds UI
        self.Sounds = Sounds(self)
        self.Sounds.show()

    # Print debug messages, if needed
    def msg(self, message):
        if DEBUG:
            print(str(datetime.time(datetime.now())) + " > DEBUG: " + message)

    # Switches the interface to edit another level.
    def change_level(self, newLevel):
        self.msg("Switching to level " + str(newLevel))
        self.levelIndex = newLevel - 1
        self.update_sets()
        self.reset_phoneme_ui()
        self.ui.listPhonemes.clear()

    # Updates the sound paths of all phonemes using the sounds config file.
    def update_sound_paths(self):
        try:
            # get the collection from the sounds config file
            with open("sounds.pk", 'rb') as input:
                collection = pickle.load(input)
                self.msg("Data loaded from sounds.pk.")
                currentSet = self.get_set()
                phonemes = currentSet.phonemes
                # for each phoneme, update the path using the text
                for i in range(0, len(phonemes)):
                    phoneme = phonemes[i]
                    # iterate through every Phoneme_Sound to find a match
                    for ps in collection:
                        if ps.text == phoneme.text:
                            phoneme.sound_path = ps.path
        except:
            self.msg("Warning: sounds config file not found.")

    # Saves the entire configuration as a file using the pickle module.
    # The file contains a single Game() object as defined in phoneme.py.
    # The object consists of a list of levels as well as values for each
    # difficulty slider (failed attempts, hints requested, and time).
    def save(self):
        # construct the game object to save
        game = Game()
        game.levels = self.levels
        game.failedAttemptsWeight = self.ui.sldrFailedAttempts.value()
        game.hintsRequestedWeight = self.ui.sldrHintsRequested.value()
        game.timeWeight = self.ui.sldrTime.value()

        # get path to save file to
        path = QtGui.QFileDialog.getSaveFileName(self, 
                                           "Save File", 
                                           "", 
                                           "Phoneme Awareness Configuration File (*.cfg)")
        path = str(path) + ".cfg"
        try:
            with open(str(path), 'wb') as output:
                pickle.dump(game, output, pickle.HIGHEST_PROTOCOL)
                self.msg("Save successful.")
        except:
            self.msg("Save failed.")

        # additionally, save the slider values into a text file
        #try:
        #    with open("sliders.txt", 'wb') as output:
        #        output.write(str(game.failedAttemptsWeight) + "\n")
        #        output.write(str(game.hintsRequestedWeight) + "\n")
        #        output.write(str(game.timeWeight) + "\n")
        #except:
        #    self.msg("Slider file output failed.")


    # Load button functionality
    def load(self):
        # get path to load file from
        path = str(QtGui.QFileDialog.getOpenFileName(self,
                                                     "Load File",
                                                     "",
                                                     "Phoneme Awareness Configuration File (*.cfg)"))

        # get game object from file
        game = None
        try:
            with open(path, 'rb') as input:
                game = pickle.load(input)
                self.levels = game.levels
                self.ui.sldrFailedAttempts.setValue(game.failedAttemptsWeight)
                self.ui.sldrHintsRequested.setValue(game.hintsRequestedWeight)
                self.ui.sldrTime.setValue(game.timeWeight)
                self.msg("Settings file loaded successfully.")
                self.update_sets()
        except:
            self.msg("Settings could not be loaded.")

    # Installs the game with the current configuration to the Sifteos
    def install(self):
         # construct the game object
        game = Game()
        game.levels = self.levels
        game.failedAttemptsWeight = self.ui.sldrFailedAttempts.value()
        game.hintsRequestedWeight = self.ui.sldrHintsRequested.value()
        game.timeWeight = self.ui.sldrTime.value()

        generate_files(game, '..\PhonemeFrenzy')
        compile_elf()

    # Allows the user to define a custom sound file
    def custom_sound(self):
        phoneme = self.get_phoneme()
        path = str(QtGui.QFileDialog.getOpenFileName())
        if path != "":
            phoneme.sound_path = path
            phoneme.text = "custom"
            self.lblSoundPath.setText(basename(path))
        

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
            phoneme = self.get_phoneme()
            phoneme.text = s
            self.update_sound_paths()
            self.ui.lblSoundPath.setText(basename(phoneme.sound_path))
            sound = QtGui.QSound(phoneme.sound_path)
            sound.play()

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
