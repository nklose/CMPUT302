"""
This script loads up the phoneme sound file interface.

This allows the user to configure which sound files are associated with which phonemes.

Code for the basic framework was borrowed from:
http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/

Code for using PyQt4 functions is from PyQt Class Reference:
http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Code for object pickling adapted from:
http://stackoverflow.com/questions/4529815/how-to-save-an-object-in-python

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys
import pickle
from PyQt4 import QtCore, QtGui
from sound_dialog import Ui_Dialog

# Object to store each phoneme sound
class Phoneme_Sound():
    def __init__(self, text = "", path = ""):
        self.text = text
        self.path = path

class Sounds(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # create a collection of Phoneme_Sound objects either by
        # loading an existing file or creating a new collection
        self.collection = None
        self.load_collection()

        # Track currently selected sound
        self.sound = None

        # deselect any currently selected phonemes
        self.deselect_all()

        # disable buttons for now
        self.ui.btnChangeFile.setEnabled(False)
        self.ui.btnPreview.setEnabled(False)

        #######################################################
        # Interface Object Connections                        #
        #######################################################

        ## Buttons

        # Phoneme Sound Buttons
        QtCore.QObject.connect(self.ui.btnA, QtCore.SIGNAL("clicked()"), self.a)
        QtCore.QObject.connect(self.ui.btnO, QtCore.SIGNAL("clicked()"), self.o)
        QtCore.QObject.connect(self.ui.btnEU, QtCore.SIGNAL("clicked()"), self.eu)
        QtCore.QObject.connect(self.ui.btnE_grave, QtCore.SIGNAL("clicked()"), 
                               self.e_grave)
        QtCore.QObject.connect(self.ui.btnE_acute, QtCore.SIGNAL("clicked()"), 
                               self.e_acute)
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

        # Preview Sound Button
        QtCore.QObject.connect(self.ui.btnPreview, 
                               QtCore.SIGNAL("clicked()"),
                               self.play_sound)

        # Change File Button
        QtCore.QObject.connect(self.ui.btnChangeFile,
                               QtCore.SIGNAL("clicked()"),
                               self.change_file)

        # Save Button
        QtCore.QObject.connect(self.ui.btnSave,
                               QtCore.SIGNAL("clicked()"),
                               self.save)

        # Cancel Button
        QtCore.QObject.connect(self.ui.btnCancel,
                               QtCore.SIGNAL("clicked()"),
                               self.cancel)

    def play_sound(self):
        print('play sound')

    # Modifies the sound file path for the selected phoneme
    def change_file(self):
        # get wav file path
        path = str(QtGui.QFileDialog.getOpenFileName(self, 
                                                     "Load Sound", 
                                                     "", 
                                                     "WAV Files (*.wav)"))
        # show path in GUI
        self.ui.lblPath.setText(path)
    
        # save the path to the current phoneme sound
        self.add_path(path)

    # Saves the collection into a file and closes the dialog
    def save(self):
        with open("sounds.pk", 'wb') as output:
            pickle.dump(self.collection, output, pickle.HIGHEST_PROTOCOL)
        self.close()

    # Loads a file into the collection, or creates a new one on failure
    def load_collection(self):
        try:
            with open("sounds.pk", 'rb') as input:
                self.collection = pickle.load(input)
                self.ui.lblPath.setText("Sounds file successfully loaded.")
        except:
            self.ui.lblPath.setText("Sounds file cannot be loaded; making a new one.")
            self.collection = self.init_collection()

    # Closes the dialog without making any changes
    def cancel(self):
        self.close()

    # Adds a given path to the currently selected phoneme sound
    def add_path(self, path):
        # Iterate through all phonemes in the collection
        for phoneme in self.collection:
            if phoneme.text == self.sound:
                phoneme.path = path
            
    # Updates the displayed path to the currently selected phoneme's
    def update_path(self):
        # Iterate through all phonemes in the collection
        for phoneme in self.collection:
            if phoneme.text == self.sound:
                self.ui.lblPath.setText(phoneme.path)

    # Initializes the collection of phonemes
    def init_collection(self):
        c = []
        c.append(Phoneme_Sound("a"))
        c.append(Phoneme_Sound("o"))
        c.append(Phoneme_Sound("eu"))
        c.append(Phoneme_Sound("e_grave"))
        c.append(Phoneme_Sound("i"))
        c.append(Phoneme_Sound("u"))
        c.append(Phoneme_Sound("ou"))
        c.append(Phoneme_Sound("an"))
        c.append(Phoneme_Sound("on"))
        c.append(Phoneme_Sound("un"))
        c.append(Phoneme_Sound("in"))
        c.append(Phoneme_Sound("e_acute"))
        c.append(Phoneme_Sound("ill"))
        c.append(Phoneme_Sound("ui"))
        c.append(Phoneme_Sound("oi"))
        c.append(Phoneme_Sound("p"))
        c.append(Phoneme_Sound("b"))
        c.append(Phoneme_Sound("f"))
        c.append(Phoneme_Sound("v"))
        c.append(Phoneme_Sound("m"))
        c.append(Phoneme_Sound("r"))
        c.append(Phoneme_Sound("t"))
        c.append(Phoneme_Sound("d"))
        c.append(Phoneme_Sound("s"))
        c.append(Phoneme_Sound("z"))
        c.append(Phoneme_Sound("n"))
        c.append(Phoneme_Sound("l"))
        c.append(Phoneme_Sound("k"))
        c.append(Phoneme_Sound("g"))
        c.append(Phoneme_Sound("ch"))
        c.append(Phoneme_Sound("j"))
        c.append(Phoneme_Sound("gn"))
        return c
 
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
        self.sound = s
        
        # enable buttons if necessary
        if s != "":
            self.ui.btnPreview.setEnabled(True)
            self.ui.btnChangeFile.setEnabled(True)

        # display path for currently selected phoneme
        self.update_path()

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
    myapp = Sounds()
    myapp.show()
    sys.exit(app.exec_())
