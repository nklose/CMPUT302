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

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        #######################################################
        # Interface Object Connections                        #
        #######################################################

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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
