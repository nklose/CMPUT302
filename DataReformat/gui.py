# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SifteoImageProcessor.ui'
#
# Created: Thu Apr 11 12:52:53 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 138)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_convert = QtGui.QPushButton(self.centralwidget)
        self.pushButton_convert.setGeometry(QtCore.QRect(670, 90, 91, 28))
        self.pushButton_convert.setObjectName(_fromUtf8("pushButton_convert"))
        self.lineEdit_title = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_title.setGeometry(QtCore.QRect(100, 90, 541, 22))
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.label_folder = QtGui.QLabel(self.centralwidget)
        self.label_folder.setGeometry(QtCore.QRect(32, 50, 61, 20))
        self.label_folder.setObjectName(_fromUtf8("label_folder"))
        self.pushButton_loadImage = QtGui.QPushButton(self.centralwidget)
        self.pushButton_loadImage.setGeometry(QtCore.QRect(100, 10, 111, 28))
        self.pushButton_loadImage.setObjectName(_fromUtf8("pushButton_loadImage"))
        self.label_imageFile = QtGui.QLabel(self.centralwidget)
        self.label_imageFile.setGeometry(QtCore.QRect(110, 50, 651, 16))
        self.label_imageFile.setText(_fromUtf8(""))
        self.label_imageFile.setObjectName(_fromUtf8("label_imageFile"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_convert.setText(_translate("MainWindow", "Convert", None))
        self.label_title.setText(_translate("MainWindow", "Title/Text: ", None))
        self.label_folder.setText(_translate("MainWindow", "Folder:", None))
        self.pushButton_loadImage.setText(_translate("MainWindow", "Load Image", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

