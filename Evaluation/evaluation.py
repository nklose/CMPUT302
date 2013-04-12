"""
This script loads up the evaluation interface.

Code for the basic framework was borrowed from:
http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/

Code for using PyQt4 functions is from PyQt Class Reference:
http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""
import sys, os
import pickle
import platform
import subprocess
from itertools import izip_longest
from savedata import getStoredObjs
from PyQt4 import QtCore, QtGui
from gui import Ui_EvaluationWindow
from user import *

# Global constants
DATA_FILE = os.path.join(".", "data.pk")
winbinpath = os.path.join('..', 'bins', 'windowsbin')
linuxbinpath = os.path.join('..', 'bins', 'linuxbin')
macbinpath = os.path.join('..', 'bins', 'macbin')


class Evaluation(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_EvaluationWindow()
        self.ui.setupUi(self)

        # Force consistent theme and font size
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setStyleSheet("font-size: 11pt")

        # Disable resizing
        self.setFixedSize(self.size())
        
        # Non-graphical interface objects
        self.users = []    # list of users
        self.userIndex = None # currently selected user
        self.playthroughIndex = None # index of selected playthrough

        # Initialize the interface
        self.initialize()

        # Object connections
        itemClicked = QtCore.SIGNAL("itemClicked(QListWidgetItem *)")
        clicked = QtCore.SIGNAL("clicked()")
        textChanged = QtCore.SIGNAL("textChanged(const QString&)")
        returnPressed = QtCore.SIGNAL("returnPressed()")

        QtCore.QObject.connect(self.ui.btnAddUser, clicked, self.add_user)
        QtCore.QObject.connect(self.ui.btnRemoveUser, clicked, self.remove_user)
        QtCore.QObject.connect(self.ui.btnAddData, clicked, self.add_data)
        QtCore.QObject.connect(self.ui.btnRemoveData, clicked, self.remove_data)

        QtCore.QObject.connect(self.ui.listUsers, itemClicked, self.select_user)
        QtCore.QObject.connect(self.ui.listPlaythroughs, itemClicked, self.select_playthrough)
        QtCore.QObject.connect(self.ui.txtNewUser, textChanged, self.check_new_user)
        QtCore.QObject.connect(self.ui.txtNewUser, returnPressed, self.add_user)

    # Initializes the GUI using the data file, or with default settings in
    #  the absence of a data file
    def initialize(self):
        try:
            with open(DATA_FILE, "rb") as input:
                self.users = pickle.load(input)
                self.refresh()
                self.msg("Local data loaded successfully.")
        except:
            self.msg("Data file not found; starting fresh.")
            self.users.append(User())
            self.refresh()

    # Adds a user to the interface.
    def add_user(self):
        if self.ui.btnAddUser.isEnabled():
            user = User(str(self.ui.txtNewUser.text()))
            self.ui.txtNewUser.clear()
            self.users.append(user)
            self.msg("Added new user: " + user.name)
            self.ui.btnAddUser.setEnabled(False)
            self.refresh()
            self.save()

    # Removes a user from the interface.
    def remove_user(self):
        title = "Remove User"
        text = "This will permanently remove all data from this user. Continue?"
        type = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
        if QtGui.QMessageBox.Yes == QtGui.QMessageBox.question(self, title, text, type):    
            if self.userIndex != None:  
                del self.users[self.userIndex]
                self.ui.btnRemoveUser.setEnabled(False)
                self.userIndex = None
                self.refresh()
                self.save()

    # Saves the current interface state.
    def save(self):
        try:
            with open(DATA_FILE, "wb") as output:
                pickle.dump(self.users, output, pickle.HIGHEST_PROTOCOL)
        except:
            self.msg("Error: couldn't save the data file.")

    # Adds one or more playthroughs from an evaluation data file.
    def add_data(self):
        # notify the user
        QtGui.QMessageBox.information(self,
                                      "Data Extraction",
                                      "Please ensure that the Sifteo Cubes are plugged into the computer using the USB cable.\n\nUser data will then be extracted from the cubes.\n\nYou will be notified when the data extraction is complete.")
        
        datafilename = "savedata.bin"
        
        # extract the data from the sifteo cubes
        try:
            binpath = getOSBinpath()
            swisspath = os.path.join(binpath, "swiss")
            print(swisspath + " savedata extract com.sifteo.phonemefrenzy " + datafilename)
            # use the "swiss savedata extract com.sifteo.sdk [file]" command to get the data
            procret = subprocess.call(swisspath + " savedata extract com.sifteo.phonemefrenzy " + datafilename)
            if procret != 0:
                raise Exception("Data extraction failed.")
        except: # if an exception occured report error to user
            QtGui.QMessageBox.information(self,
                                      "Data Extraction Error",
                                      "An error has occured while attempting to extract data from the cubes.\n\nPlease make sure the Sifteo Cubes were plugged in correctly and attempt extraction again.\n")
        else:   # if no exception, report to user success
            QtGui.QMessageBox.information(self,
                                          "Data Extraction",
                                          "Data extraction has completed successfully.")
        
        # get only the first 30 integers which are relevant
        shortObjs = []
        storedObjs = getStoredObjs(datafilename)
        for lst in storedObjs:
            shortObjs.append(lst[:30])

        # separate playthrough num object from level records objects
        levelObjects = shortObjs[:10]
        playthroughNum = shortObjs[-1][0]

        # group level data by 3s to account for [attemps, hints, time]
        lvlObjs = []
        for obj in levelObjects:
            tempObj = list(grouper(3, obj))
            lvlObjs.append(tempObj)
        
        # put in ascending level order
        lvlObjs.reverse()

        # sort ResultData into levels from sorting by playthrough
        levels = []
        for x in range(0,10):
            level = []
            for y in range(0,playthroughNum):
                level.append(lvlObjs[x][y])
            levels.append(level)
        
        # get current user so we can start adding data to the UI
        user = self.get_user()

        # translate list of levels into evaluation UI objects
        for x in range(0,playthroughNum):
            play = Playthrough()
            lvls = play.level
            for lvl in range(0, 10):
                group = lvls[lvl]
                group.attempts = levels[lvl][x][0]
                group.hints = levels[lvl][x][1]
                group.time = levels[lvl][x][2]
            user.playthroughs.append(play)
        
        # update visible data, and then save it to the file
        self.refresh()
        self.save()
    
    # Removes a specific playthrough from the selected user.
    def remove_data(self):
        self.ui.btnRemoveData.setEnabled(False)
        u = self.get_user()
        del u.playthroughs[self.playthroughIndex]
        self.playthroughIndex = None
        self.refresh()
        self.save()

    # Returns the index of a given user as an integer.
    def user_index(self, item):
        for i in range(0, len(self.users)):
            user = self.users[i]
            if user.name == str(item.text()):
                return i
        return None

    # Returns the currently selected user object.
    def get_user(self):
        if self.userIndex != None:
            return self.users[self.userIndex]
        else:
            return None

    # Returns the currently selected playthrough object.
    def get_playthrough(self):
        u = self.get_user()
        return u.playthroughs[self.playthroughIndex]

    # Checks to see whether the currently entered string for a new user matches
    #  any existing users, and temporarily disables adding until it's made unique
    def check_new_user(self, text):
        if str(text) != "":
            unique = True
            if self.users != None:
                for u in range(0, len(self.users)):
                    user = self.users[u]
                    if user.name == str(text):
                        unique = False
            if unique:
                self.ui.btnAddUser.setEnabled(True)
            else:
                self.ui.btnAddUser.setEnabled(False)
        else:
            self.ui.btnAddUser.setEnabled(False)

    # Refreshes the interface to show the current program state.
    def refresh(self):
        self.ui.listUsers.clear()
        for user in self.users:
            self.ui.listUsers.addItem(user.name)

        self.ui.listPlaythroughs.clear()
        u = self.get_user()
        if u != None:
            i = 0
            for p in u.playthroughs:
                self.ui.listPlaythroughs.addItem(p.name)
                p.index = i
                i += 1
            self.ui.listUsers.item(self.userIndex).setSelected(True)

    # Displays a message to the user via the message box
    def msg(self, text):
        self.ui.lblMessage.setText(str(text))

    # Selects a specific user from the list of users.
    def select_user(self, user):
        self.ui.btnRemoveUser.setEnabled(True)
        index = self.user_index(user)
        self.userIndex = index
        self.refresh()

    # Selects a specific playthrough from the list of playthroughs.
    # Update the UI based on selected user's attributes
    def select_playthrough(self, playthrough):
        self.ui.btnRemoveData.setEnabled(True)
        
        self.playthroughIndex = self.ui.listPlaythroughs.selectedIndexes()[0].row()
        
        p = self.get_playthrough()
        
        index = p.index
        self.playthroughIndex = index
        
        # Make lists for every level-specific UI element
        hints = [self.ui.lblHintsLevel1, self.ui.lblHintsLevel2,
                 self.ui.lblHintsLevel3, self.ui.lblHintsLevel4,
                 self.ui.lblHintsLevel5, self.ui.lblHintsLevel6,
                 self.ui.lblHintsLevel7, self.ui.lblHintsLevel8,
                 self.ui.lblHintsLevel9, self.ui.lblHintsLevel10]
        attempts = [self.ui.lblAttemptsLevel1, self.ui.lblAttemptsLevel2,
                    self.ui.lblAttemptsLevel3, self.ui.lblAttemptsLevel4,
                    self.ui.lblAttemptsLevel5, self.ui.lblAttemptsLevel6,
                    self.ui.lblAttemptsLevel7, self.ui.lblAttemptsLevel8,
                    self.ui.lblAttemptsLevel9, self.ui.lblAttemptsLevel10]
        times = [self.ui.lblTimeLevel1, self.ui.lblTimeLevel2,
                 self.ui.lblTimeLevel3, self.ui.lblTimeLevel4,
                 self.ui.lblTimeLevel5, self.ui.lblTimeLevel6,
                 self.ui.lblTimeLevel7, self.ui.lblTimeLevel8,
                 self.ui.lblTimeLevel9, self.ui.lblTimeLevel10]
        
        hintTotal = 0
        attemptTotal = 0
        timeTotal = 0

        for i in range(0, 10):
            hint = hints[i]
            attempt = attempts[i]
            time = times[i]

            hint.setText(str(p.level[i].hints))
            attempt.setText(str(p.level[i].attempts))
            time.setText(str(p.level[i].time))

            hintTotal += p.level[i].hints
            attemptTotal += p.level[i].attempts
            timeTotal += p.level[i].time

        hintAverage = float(hintTotal / 10)
        attemptAverage = float(attemptTotal / 10)
        timeAverage = float(timeTotal / 10)

        self.ui.lblHintsTotal.setText(str(hintTotal))
        self.ui.lblAttemptsTotal.setText(str(attemptTotal))
        self.ui.lblTimeTotal.setText(str(timeTotal))
        self.ui.lblHintsAverage.setText(str(hintAverage))
        self.ui.lblAttemptsAverage.setText(str(attemptAverage))
        self.ui.lblTimeAverage.setText(str(timeAverage))

def getOSBinpath():
    # detect which OS to determine which executables to use
    ostype = platform.system()

    if (ostype == 'Windows'):
            return winbinpath
    elif (ostype == 'Linux'):
            return linuxbinpath
    elif (ostype == 'Darwin'):	# This is Mac OSX
            return macbinpath


def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

# Start up the interface
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    evaluation = Evaluation()
    evaluation.show()
    sys.exit(app.exec_())
