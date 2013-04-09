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
from PyQt4 import QtCore, QtGui
from gui import Ui_EvaluationWindow
from user import *

# Global constants
DATA_FILE = os.path.join(".", "data.pk")

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
        self.userIndex = 0 # currently selected user

        # Initialize the interface
        self.initialize()

        # Object connections
        itemClicked = QtCore.SIGNAL("itemClicked(QListWidgetItem *)")
        clicked = QtCore.SIGNAL("clicked()")
        textChanged = QtCore.SIGNAL("textChanged(const QString&)")
        returnPressed = QtCore.SIGNAL("returnPressed()")

        QtCore.QObject.connect(self.ui.btnAddUser, clicked, self.add_user)
        QtCore.QObject.connect(self.ui.btnRemoveUser, clicked, self.remove_user)
        QtCore.QObject.connect(self.ui.btnSave, clicked, self.save)
        QtCore.QObject.connect(self.ui.btnAddData, clicked, self.add_data)
        QtCore.QObject.connect(self.ui.btnClearData, clicked, self.clear_data)

        QtCore.QObject.connect(self.ui.listUsers, itemClicked, self.select_user)
        QtCore.QObject.connect(self.ui.txtNewUser, textChanged, self.check_new_user)
        QtCore.QObject.connect(self.ui.txtNewUser, returnPressed, self.add_user)

    # Initializes the GUI using the data file, or with default settings in
    #  the absense of a data file
    def initialize(self):
        try:
            open(DATA_FILE)
        except:
            self.msg("Data file not found; creating a new one.")
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

    # Removes a user from the interface.
    def remove_user(self):
        title = "Remove User"
        text = "This will permanently remove all data from this user. Continue?"
        type = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
        if QtGui.QMessageBox.Yes == QtGui.QMessageBox.question(self, title, text, type):
            if self.userIndex != None:  
                del self.users[self.userIndex]
                self.ui.btnRemoveUser.setEnabled(False)
                self.refresh()

    # Saves the current interface state.
    def save(self):
        pass

    # Adds data from an evaluation file to the current user's statistics.
    def add_data(self):
        pass
    
    # Clears all data from the current user and refreshes the interface.
    def clear_data(self):
        pass

    # Returns the index of a given user as an integer.
    def user_index(self, item):
        for i in range(0, len(self.users)):
            user = self.users[i]
            if user.name == str(item.text()):
                return i
        return None

    # Returns the currently selected user object.
    def get_user(self):
        return self.users[self.userIndex]

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

    # Displays a message to the user via the message box
    def msg(self, text):
        self.ui.lblMessage.setText(str(text))

    # Selects a specific user from the list of users.
    def select_user(self, user):
        self.ui.btnRemoveUser.setEnabled(True)
        index = self.user_index(user)
        self.userIndex = index
        
        # Update the UI based on selected user's attributes
        u = self.get_user()
        self.ui.lblHintsTotal.setText(str(u.total.hints))
        self.ui.lblAttemptsTotal.setText(str(u.total.attempts))
        self.ui.lblTimeTotal.setText(str(u.total.time))
        self.ui.lblHintsAverage.setText(str(u.average.hints))
        self.ui.lblAttemptsAverage.setText(str(u.average.attempts))
        self.ui.lblTimeAverage.setText(str(u.average.time))

# Start up the interface
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    evaluation = Evaluation()
    evaluation.show()
    sys.exit(app.exec_())
