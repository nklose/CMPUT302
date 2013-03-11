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
from customization_gui import Ui_mainWindow
from os.path import basename
from phoneme_set import *

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Make settings frame invisible until a set is selected
        self.ui.frame.setVisible(0)

        # Instantiate the set of phoneme sets, and add the first
        # one to the list of sets.
        self.sets = [Phoneme_Set()]
        self.update_sets()

        #######################################################
        # Interface Object Connections                        #
        #######################################################

        ## List Widget
        QtCore.QObject.connect(self.ui.listSets,
                               QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),
                               self.select_item)

        ## Buttons
		# Load Goal Image
        QtCore.QObject.connect(self.ui.btnLoadGoalImage,
                               QtCore.SIGNAL("clicked()"),
                               self.load_goal_image)

	# Designates an image to be the goal image for the current set.
    def load_goal_image(self, set):
        path = str(QtGui.QFileDialog.getOpenFileName())
        file = basename(path)
        self.ui.imgGoal.setPixmap(QtGui.QPixmap(path))

    # Updates the displayed list of sets with the internal list.
    def update_sets(self):
        self.ui.listSets.clear()
        index = 1
        for item in self.sets:
            self.ui.listSets.addItem("Set " + str(index))
            index += 1

    # This function is called when the user selects a specific item
    # from the list of sets.
    def select_item(self, item):
        # show frame if it isn't there already
        self.ui.frame.setVisible(1)

        # get the index of the selected item
        index = self.index_from_item(item)

        # load the goal for the selected item
        #self.ui.lblGoalImagePath.text(self.sets[index].goal.image_path)
        goal_image_path = self.sets[index].goal.image_path
        self.ui.lblGoalImagePath.setText(goal_image_path)
        goal_sound_path = self.sets[index].goal.sound_path
        self.ui.lblGoalSoundPath.setText(goal_sound_path)
        
        # load the image, if available
        if goal_image_path != "<none>":
            self.ui.imgGoal.setPixmap(QtGui.QPixmap(goal_image_path))
        

    # Returns the index if a given item as an integer.
    def index_from_item(self, item):
        return int(item.text()[4:]) - 1

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
