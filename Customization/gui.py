# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Apr 11 22:50:33 2013
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(980, 660)
        self.btnSave = QtGui.QPushButton(mainWindow)
        self.btnSave.setGeometry(QtCore.QRect(10, 600, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.btnLoad = QtGui.QPushButton(mainWindow)
        self.btnLoad.setGeometry(QtCore.QRect(240, 600, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLoad.setFont(font)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.btnInstall = QtGui.QPushButton(mainWindow)
        self.btnInstall.setGeometry(QtCore.QRect(760, 600, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnInstall.setFont(font)
        self.btnInstall.setObjectName(_fromUtf8("btnInstall"))
        self.labelLevel4 = QtGui.QLabel(mainWindow)
        self.labelLevel4.setGeometry(QtCore.QRect(60, 210, 46, 13))
        self.labelLevel4.setObjectName(_fromUtf8("labelLevel4"))
        self.labelLevel8 = QtGui.QLabel(mainWindow)
        self.labelLevel8.setGeometry(QtCore.QRect(60, 450, 46, 31))
        self.labelLevel8.setObjectName(_fromUtf8("labelLevel8"))
        self.labelLevel7 = QtGui.QLabel(mainWindow)
        self.labelLevel7.setGeometry(QtCore.QRect(60, 390, 46, 31))
        self.labelLevel7.setObjectName(_fromUtf8("labelLevel7"))
        self.labelLevel10 = QtGui.QLabel(mainWindow)
        self.labelLevel10.setGeometry(QtCore.QRect(60, 570, 46, 31))
        self.labelLevel10.setObjectName(_fromUtf8("labelLevel10"))
        self.groupBox = QtGui.QGroupBox(mainWindow)
        self.groupBox.setGeometry(QtCore.QRect(100, 350, 251, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblFailedAttempts = QtGui.QLabel(self.groupBox)
        self.lblFailedAttempts.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.lblFailedAttempts.setObjectName(_fromUtf8("lblFailedAttempts"))
        self.sldrFailedAttempts = QtGui.QSlider(self.groupBox)
        self.sldrFailedAttempts.setGeometry(QtCore.QRect(10, 50, 191, 29))
        self.sldrFailedAttempts.setMaximum(100)
        self.sldrFailedAttempts.setProperty("value", 50)
        self.sldrFailedAttempts.setOrientation(QtCore.Qt.Horizontal)
        self.sldrFailedAttempts.setObjectName(_fromUtf8("sldrFailedAttempts"))
        self.lblHintsRequested = QtGui.QLabel(self.groupBox)
        self.lblHintsRequested.setGeometry(QtCore.QRect(10, 100, 141, 17))
        self.lblHintsRequested.setObjectName(_fromUtf8("lblHintsRequested"))
        self.sldrHintsRequested = QtGui.QSlider(self.groupBox)
        self.sldrHintsRequested.setGeometry(QtCore.QRect(10, 120, 191, 29))
        self.sldrHintsRequested.setMaximum(100)
        self.sldrHintsRequested.setProperty("value", 50)
        self.sldrHintsRequested.setOrientation(QtCore.Qt.Horizontal)
        self.sldrHintsRequested.setObjectName(_fromUtf8("sldrHintsRequested"))
        self.lblTime = QtGui.QLabel(self.groupBox)
        self.lblTime.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.lblTime.setObjectName(_fromUtf8("lblTime"))
        self.sldrTime = QtGui.QSlider(self.groupBox)
        self.sldrTime.setGeometry(QtCore.QRect(10, 190, 191, 29))
        self.sldrTime.setMaximum(100)
        self.sldrTime.setProperty("value", 50)
        self.sldrTime.setOrientation(QtCore.Qt.Horizontal)
        self.sldrTime.setObjectName(_fromUtf8("sldrTime"))
        self.lblAttempts = QtGui.QLabel(self.groupBox)
        self.lblAttempts.setGeometry(QtCore.QRect(210, 50, 31, 31))
        self.lblAttempts.setObjectName(_fromUtf8("lblAttempts"))
        self.lblHints = QtGui.QLabel(self.groupBox)
        self.lblHints.setGeometry(QtCore.QRect(210, 120, 31, 31))
        self.lblHints.setObjectName(_fromUtf8("lblHints"))
        self.lblTimeValue = QtGui.QLabel(self.groupBox)
        self.lblTimeValue.setGeometry(QtCore.QRect(210, 190, 31, 31))
        self.lblTimeValue.setObjectName(_fromUtf8("lblTimeValue"))
        self.frame = QtGui.QFrame(mainWindow)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(370, 20, 601, 571))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btnSetGoal = QtGui.QPushButton(self.frame)
        self.btnSetGoal.setEnabled(False)
        self.btnSetGoal.setGeometry(QtCore.QRect(60, 530, 151, 31))
        self.btnSetGoal.setObjectName(_fromUtf8("btnSetGoal"))
        self.listPhonemes = QtGui.QListWidget(self.frame)
        self.listPhonemes.setGeometry(QtCore.QRect(10, 50, 251, 471))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listPhonemes.setFont(font)
        self.listPhonemes.setAlternatingRowColors(True)
        self.listPhonemes.setViewMode(QtGui.QListView.ListMode)
        self.listPhonemes.setObjectName(_fromUtf8("listPhonemes"))
        item = QtGui.QListWidgetItem()
        self.listPhonemes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listPhonemes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listPhonemes.addItem(item)
        self.btnRemovePhoneme = QtGui.QPushButton(self.frame)
        self.btnRemovePhoneme.setEnabled(False)
        self.btnRemovePhoneme.setGeometry(QtCore.QRect(230, 10, 31, 31))
        self.btnRemovePhoneme.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemovePhoneme.setIcon(icon)
        self.btnRemovePhoneme.setIconSize(QtCore.QSize(24, 24))
        self.btnRemovePhoneme.setObjectName(_fromUtf8("btnRemovePhoneme"))
        self.txtNewPhoneme = QtGui.QLineEdit(self.frame)
        self.txtNewPhoneme.setGeometry(QtCore.QRect(10, 10, 171, 27))
        self.txtNewPhoneme.setObjectName(_fromUtf8("txtNewPhoneme"))
        self.btnAddPhoneme = QtGui.QPushButton(self.frame)
        self.btnAddPhoneme.setEnabled(False)
        self.btnAddPhoneme.setGeometry(QtCore.QRect(190, 10, 31, 31))
        self.btnAddPhoneme.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddPhoneme.setIcon(icon1)
        self.btnAddPhoneme.setIconSize(QtCore.QSize(24, 24))
        self.btnAddPhoneme.setObjectName(_fromUtf8("btnAddPhoneme"))
        self.soundsGroup = QtGui.QGroupBox(self.frame)
        self.soundsGroup.setEnabled(False)
        self.soundsGroup.setGeometry(QtCore.QRect(280, 10, 301, 291))
        self.soundsGroup.setObjectName(_fromUtf8("soundsGroup"))
        self.btnA = QtGui.QPushButton(self.soundsGroup)
        self.btnA.setGeometry(QtCore.QRect(10, 30, 31, 27))
        self.btnA.setAcceptDrops(False)
        self.btnA.setCheckable(True)
        self.btnA.setChecked(False)
        self.btnA.setAutoDefault(True)
        self.btnA.setDefault(False)
        self.btnA.setFlat(False)
        self.btnA.setObjectName(_fromUtf8("btnA"))
        self.btnO = QtGui.QPushButton(self.soundsGroup)
        self.btnO.setGeometry(QtCore.QRect(40, 30, 31, 27))
        self.btnO.setAcceptDrops(False)
        self.btnO.setCheckable(True)
        self.btnO.setChecked(False)
        self.btnO.setAutoDefault(True)
        self.btnO.setDefault(False)
        self.btnO.setFlat(False)
        self.btnO.setObjectName(_fromUtf8("btnO"))
        self.btnEU = QtGui.QPushButton(self.soundsGroup)
        self.btnEU.setGeometry(QtCore.QRect(70, 30, 31, 27))
        self.btnEU.setAcceptDrops(False)
        self.btnEU.setCheckable(True)
        self.btnEU.setChecked(False)
        self.btnEU.setAutoDefault(True)
        self.btnEU.setDefault(False)
        self.btnEU.setFlat(False)
        self.btnEU.setObjectName(_fromUtf8("btnEU"))
        self.btnE_grave = QtGui.QPushButton(self.soundsGroup)
        self.btnE_grave.setGeometry(QtCore.QRect(100, 30, 31, 27))
        self.btnE_grave.setAcceptDrops(False)
        self.btnE_grave.setCheckable(True)
        self.btnE_grave.setChecked(False)
        self.btnE_grave.setAutoDefault(True)
        self.btnE_grave.setDefault(False)
        self.btnE_grave.setFlat(False)
        self.btnE_grave.setObjectName(_fromUtf8("btnE_grave"))
        self.btnE_acute = QtGui.QPushButton(self.soundsGroup)
        self.btnE_acute.setGeometry(QtCore.QRect(140, 70, 31, 27))
        self.btnE_acute.setAcceptDrops(False)
        self.btnE_acute.setCheckable(True)
        self.btnE_acute.setChecked(False)
        self.btnE_acute.setAutoDefault(True)
        self.btnE_acute.setDefault(False)
        self.btnE_acute.setFlat(False)
        self.btnE_acute.setObjectName(_fromUtf8("btnE_acute"))
        self.btnE = QtGui.QPushButton(self.soundsGroup)
        self.btnE.setGeometry(QtCore.QRect(140, 30, 31, 27))
        self.btnE.setAcceptDrops(False)
        self.btnE.setCheckable(True)
        self.btnE.setChecked(False)
        self.btnE.setAutoDefault(True)
        self.btnE.setDefault(False)
        self.btnE.setFlat(False)
        self.btnE.setObjectName(_fromUtf8("btnE"))
        self.btnI = QtGui.QPushButton(self.soundsGroup)
        self.btnI.setGeometry(QtCore.QRect(180, 30, 41, 27))
        self.btnI.setAcceptDrops(False)
        self.btnI.setCheckable(True)
        self.btnI.setChecked(False)
        self.btnI.setAutoDefault(True)
        self.btnI.setDefault(False)
        self.btnI.setFlat(False)
        self.btnI.setObjectName(_fromUtf8("btnI"))
        self.btnU = QtGui.QPushButton(self.soundsGroup)
        self.btnU.setGeometry(QtCore.QRect(220, 30, 31, 27))
        self.btnU.setAcceptDrops(False)
        self.btnU.setCheckable(True)
        self.btnU.setChecked(False)
        self.btnU.setAutoDefault(True)
        self.btnU.setDefault(False)
        self.btnU.setFlat(False)
        self.btnU.setObjectName(_fromUtf8("btnU"))
        self.btnOU = QtGui.QPushButton(self.soundsGroup)
        self.btnOU.setGeometry(QtCore.QRect(250, 30, 41, 27))
        self.btnOU.setAcceptDrops(False)
        self.btnOU.setCheckable(True)
        self.btnOU.setChecked(False)
        self.btnOU.setAutoDefault(True)
        self.btnOU.setDefault(False)
        self.btnOU.setFlat(False)
        self.btnOU.setObjectName(_fromUtf8("btnOU"))
        self.btnAN = QtGui.QPushButton(self.soundsGroup)
        self.btnAN.setGeometry(QtCore.QRect(10, 70, 31, 27))
        self.btnAN.setAcceptDrops(False)
        self.btnAN.setCheckable(True)
        self.btnAN.setChecked(False)
        self.btnAN.setAutoDefault(True)
        self.btnAN.setDefault(False)
        self.btnAN.setFlat(False)
        self.btnAN.setObjectName(_fromUtf8("btnAN"))
        self.btnON = QtGui.QPushButton(self.soundsGroup)
        self.btnON.setGeometry(QtCore.QRect(40, 70, 31, 27))
        self.btnON.setAcceptDrops(False)
        self.btnON.setCheckable(True)
        self.btnON.setChecked(False)
        self.btnON.setAutoDefault(True)
        self.btnON.setDefault(False)
        self.btnON.setFlat(False)
        self.btnON.setObjectName(_fromUtf8("btnON"))
        self.btnUN = QtGui.QPushButton(self.soundsGroup)
        self.btnUN.setGeometry(QtCore.QRect(70, 70, 31, 27))
        self.btnUN.setAcceptDrops(False)
        self.btnUN.setCheckable(True)
        self.btnUN.setChecked(False)
        self.btnUN.setAutoDefault(True)
        self.btnUN.setDefault(False)
        self.btnUN.setFlat(False)
        self.btnUN.setObjectName(_fromUtf8("btnUN"))
        self.btnIN = QtGui.QPushButton(self.soundsGroup)
        self.btnIN.setGeometry(QtCore.QRect(100, 70, 31, 27))
        self.btnIN.setAcceptDrops(False)
        self.btnIN.setCheckable(True)
        self.btnIN.setChecked(False)
        self.btnIN.setAutoDefault(True)
        self.btnIN.setDefault(False)
        self.btnIN.setFlat(False)
        self.btnIN.setObjectName(_fromUtf8("btnIN"))
        self.btnILL = QtGui.QPushButton(self.soundsGroup)
        self.btnILL.setGeometry(QtCore.QRect(180, 70, 41, 27))
        self.btnILL.setAcceptDrops(False)
        self.btnILL.setCheckable(True)
        self.btnILL.setChecked(False)
        self.btnILL.setAutoDefault(True)
        self.btnILL.setDefault(False)
        self.btnILL.setFlat(False)
        self.btnILL.setObjectName(_fromUtf8("btnILL"))
        self.btnUI = QtGui.QPushButton(self.soundsGroup)
        self.btnUI.setGeometry(QtCore.QRect(220, 70, 31, 27))
        self.btnUI.setAcceptDrops(False)
        self.btnUI.setCheckable(True)
        self.btnUI.setChecked(False)
        self.btnUI.setAutoDefault(True)
        self.btnUI.setDefault(False)
        self.btnUI.setFlat(False)
        self.btnUI.setObjectName(_fromUtf8("btnUI"))
        self.btnOI = QtGui.QPushButton(self.soundsGroup)
        self.btnOI.setGeometry(QtCore.QRect(250, 70, 41, 27))
        self.btnOI.setAcceptDrops(False)
        self.btnOI.setCheckable(True)
        self.btnOI.setChecked(False)
        self.btnOI.setAutoDefault(True)
        self.btnOI.setDefault(False)
        self.btnOI.setFlat(False)
        self.btnOI.setObjectName(_fromUtf8("btnOI"))
        self.btnP = QtGui.QPushButton(self.soundsGroup)
        self.btnP.setGeometry(QtCore.QRect(10, 110, 31, 27))
        self.btnP.setAcceptDrops(False)
        self.btnP.setCheckable(True)
        self.btnP.setChecked(False)
        self.btnP.setAutoDefault(True)
        self.btnP.setDefault(False)
        self.btnP.setFlat(False)
        self.btnP.setObjectName(_fromUtf8("btnP"))
        self.btnB = QtGui.QPushButton(self.soundsGroup)
        self.btnB.setGeometry(QtCore.QRect(40, 110, 31, 27))
        self.btnB.setAcceptDrops(False)
        self.btnB.setCheckable(True)
        self.btnB.setChecked(False)
        self.btnB.setAutoDefault(True)
        self.btnB.setDefault(False)
        self.btnB.setFlat(False)
        self.btnB.setObjectName(_fromUtf8("btnB"))
        self.btnF = QtGui.QPushButton(self.soundsGroup)
        self.btnF.setGeometry(QtCore.QRect(70, 110, 31, 27))
        self.btnF.setAcceptDrops(False)
        self.btnF.setCheckable(True)
        self.btnF.setChecked(False)
        self.btnF.setAutoDefault(True)
        self.btnF.setDefault(False)
        self.btnF.setFlat(False)
        self.btnF.setObjectName(_fromUtf8("btnF"))
        self.btnV = QtGui.QPushButton(self.soundsGroup)
        self.btnV.setGeometry(QtCore.QRect(110, 110, 31, 27))
        self.btnV.setAcceptDrops(False)
        self.btnV.setCheckable(True)
        self.btnV.setChecked(False)
        self.btnV.setAutoDefault(True)
        self.btnV.setDefault(False)
        self.btnV.setFlat(False)
        self.btnV.setObjectName(_fromUtf8("btnV"))
        self.btnM = QtGui.QPushButton(self.soundsGroup)
        self.btnM.setGeometry(QtCore.QRect(140, 110, 31, 27))
        self.btnM.setAcceptDrops(False)
        self.btnM.setCheckable(True)
        self.btnM.setChecked(False)
        self.btnM.setAutoDefault(True)
        self.btnM.setDefault(False)
        self.btnM.setFlat(False)
        self.btnM.setObjectName(_fromUtf8("btnM"))
        self.btnR = QtGui.QPushButton(self.soundsGroup)
        self.btnR.setGeometry(QtCore.QRect(170, 110, 31, 27))
        self.btnR.setAcceptDrops(False)
        self.btnR.setCheckable(True)
        self.btnR.setChecked(False)
        self.btnR.setAutoDefault(True)
        self.btnR.setDefault(False)
        self.btnR.setFlat(False)
        self.btnR.setObjectName(_fromUtf8("btnR"))
        self.btnT = QtGui.QPushButton(self.soundsGroup)
        self.btnT.setGeometry(QtCore.QRect(10, 150, 31, 27))
        self.btnT.setAcceptDrops(False)
        self.btnT.setCheckable(True)
        self.btnT.setChecked(False)
        self.btnT.setAutoDefault(True)
        self.btnT.setDefault(False)
        self.btnT.setFlat(False)
        self.btnT.setObjectName(_fromUtf8("btnT"))
        self.btnD = QtGui.QPushButton(self.soundsGroup)
        self.btnD.setGeometry(QtCore.QRect(40, 150, 31, 27))
        self.btnD.setAcceptDrops(False)
        self.btnD.setCheckable(True)
        self.btnD.setChecked(False)
        self.btnD.setAutoDefault(True)
        self.btnD.setDefault(False)
        self.btnD.setFlat(False)
        self.btnD.setObjectName(_fromUtf8("btnD"))
        self.btnS = QtGui.QPushButton(self.soundsGroup)
        self.btnS.setGeometry(QtCore.QRect(70, 150, 31, 27))
        self.btnS.setAcceptDrops(False)
        self.btnS.setCheckable(True)
        self.btnS.setChecked(False)
        self.btnS.setAutoDefault(True)
        self.btnS.setDefault(False)
        self.btnS.setFlat(False)
        self.btnS.setObjectName(_fromUtf8("btnS"))
        self.btnZ = QtGui.QPushButton(self.soundsGroup)
        self.btnZ.setGeometry(QtCore.QRect(110, 150, 31, 27))
        self.btnZ.setAcceptDrops(False)
        self.btnZ.setCheckable(True)
        self.btnZ.setChecked(False)
        self.btnZ.setAutoDefault(True)
        self.btnZ.setDefault(False)
        self.btnZ.setFlat(False)
        self.btnZ.setObjectName(_fromUtf8("btnZ"))
        self.btnN = QtGui.QPushButton(self.soundsGroup)
        self.btnN.setGeometry(QtCore.QRect(140, 150, 31, 27))
        self.btnN.setAcceptDrops(False)
        self.btnN.setCheckable(True)
        self.btnN.setChecked(False)
        self.btnN.setAutoDefault(True)
        self.btnN.setDefault(False)
        self.btnN.setFlat(False)
        self.btnN.setObjectName(_fromUtf8("btnN"))
        self.btnL = QtGui.QPushButton(self.soundsGroup)
        self.btnL.setGeometry(QtCore.QRect(170, 150, 31, 27))
        self.btnL.setAcceptDrops(False)
        self.btnL.setCheckable(True)
        self.btnL.setChecked(False)
        self.btnL.setAutoDefault(True)
        self.btnL.setDefault(False)
        self.btnL.setFlat(False)
        self.btnL.setObjectName(_fromUtf8("btnL"))
        self.btnK = QtGui.QPushButton(self.soundsGroup)
        self.btnK.setGeometry(QtCore.QRect(10, 190, 31, 27))
        self.btnK.setAcceptDrops(False)
        self.btnK.setCheckable(True)
        self.btnK.setChecked(False)
        self.btnK.setAutoDefault(True)
        self.btnK.setDefault(False)
        self.btnK.setFlat(False)
        self.btnK.setObjectName(_fromUtf8("btnK"))
        self.btnG = QtGui.QPushButton(self.soundsGroup)
        self.btnG.setGeometry(QtCore.QRect(40, 190, 31, 27))
        self.btnG.setAcceptDrops(False)
        self.btnG.setCheckable(True)
        self.btnG.setChecked(False)
        self.btnG.setAutoDefault(True)
        self.btnG.setDefault(False)
        self.btnG.setFlat(False)
        self.btnG.setObjectName(_fromUtf8("btnG"))
        self.btnCH = QtGui.QPushButton(self.soundsGroup)
        self.btnCH.setGeometry(QtCore.QRect(70, 190, 31, 27))
        self.btnCH.setAcceptDrops(False)
        self.btnCH.setCheckable(True)
        self.btnCH.setChecked(False)
        self.btnCH.setAutoDefault(True)
        self.btnCH.setDefault(False)
        self.btnCH.setFlat(False)
        self.btnCH.setObjectName(_fromUtf8("btnCH"))
        self.btnJ = QtGui.QPushButton(self.soundsGroup)
        self.btnJ.setGeometry(QtCore.QRect(110, 190, 31, 27))
        self.btnJ.setAcceptDrops(False)
        self.btnJ.setCheckable(True)
        self.btnJ.setChecked(False)
        self.btnJ.setAutoDefault(True)
        self.btnJ.setDefault(False)
        self.btnJ.setFlat(False)
        self.btnJ.setObjectName(_fromUtf8("btnJ"))
        self.btnGN = QtGui.QPushButton(self.soundsGroup)
        self.btnGN.setGeometry(QtCore.QRect(140, 190, 31, 27))
        self.btnGN.setAcceptDrops(False)
        self.btnGN.setCheckable(True)
        self.btnGN.setChecked(False)
        self.btnGN.setAutoDefault(True)
        self.btnGN.setDefault(False)
        self.btnGN.setFlat(False)
        self.btnGN.setObjectName(_fromUtf8("btnGN"))
        self.lblSoundPath = QtGui.QLabel(self.soundsGroup)
        self.lblSoundPath.setGeometry(QtCore.QRect(10, 220, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.lblSoundPath.setFont(font)
        self.lblSoundPath.setFrameShape(QtGui.QFrame.Panel)
        self.lblSoundPath.setFrameShadow(QtGui.QFrame.Raised)
        self.lblSoundPath.setText(_fromUtf8(""))
        self.lblSoundPath.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSoundPath.setWordWrap(True)
        self.lblSoundPath.setObjectName(_fromUtf8("lblSoundPath"))
        self.btnModifySounds = QtGui.QPushButton(self.soundsGroup)
        self.btnModifySounds.setGeometry(QtCore.QRect(10, 260, 281, 27))
        self.btnModifySounds.setObjectName(_fromUtf8("btnModifySounds"))
        self.btnCustom = QtGui.QPushButton(self.soundsGroup)
        self.btnCustom.setGeometry(QtCore.QRect(200, 190, 91, 27))
        self.btnCustom.setObjectName(_fromUtf8("btnCustom"))
        self.imageGroup = QtGui.QGroupBox(self.frame)
        self.imageGroup.setEnabled(False)
        self.imageGroup.setGeometry(QtCore.QRect(280, 310, 301, 241))
        self.imageGroup.setObjectName(_fromUtf8("imageGroup"))
        self.imgPhoneme = QtGui.QLabel(self.imageGroup)
        self.imgPhoneme.setGeometry(QtCore.QRect(10, 30, 151, 151))
        self.imgPhoneme.setFrameShape(QtGui.QFrame.Panel)
        self.imgPhoneme.setFrameShadow(QtGui.QFrame.Raised)
        self.imgPhoneme.setText(_fromUtf8(""))
        self.imgPhoneme.setScaledContents(True)
        self.imgPhoneme.setObjectName(_fromUtf8("imgPhoneme"))
        self.btnLoadImage = QtGui.QPushButton(self.imageGroup)
        self.btnLoadImage.setEnabled(False)
        self.btnLoadImage.setGeometry(QtCore.QRect(170, 30, 131, 31))
        self.btnLoadImage.setObjectName(_fromUtf8("btnLoadImage"))
        self.lblImagePath = QtGui.QLabel(self.imageGroup)
        self.lblImagePath.setGeometry(QtCore.QRect(10, 200, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.lblImagePath.setFont(font)
        self.lblImagePath.setFrameShape(QtGui.QFrame.Panel)
        self.lblImagePath.setFrameShadow(QtGui.QFrame.Raised)
        self.lblImagePath.setText(_fromUtf8(""))
        self.lblImagePath.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImagePath.setWordWrap(True)
        self.lblImagePath.setObjectName(_fromUtf8("lblImagePath"))
        self.btnAddSet = QtGui.QPushButton(mainWindow)
        self.btnAddSet.setGeometry(QtCore.QRect(310, 310, 41, 41))
        self.btnAddSet.setText(_fromUtf8(""))
        self.btnAddSet.setIcon(icon1)
        self.btnAddSet.setIconSize(QtCore.QSize(32, 32))
        self.btnAddSet.setObjectName(_fromUtf8("btnAddSet"))
        self.labelLevel2 = QtGui.QLabel(mainWindow)
        self.labelLevel2.setGeometry(QtCore.QRect(60, 90, 46, 13))
        self.labelLevel2.setObjectName(_fromUtf8("labelLevel2"))
        self.labelLevel9 = QtGui.QLabel(mainWindow)
        self.labelLevel9.setGeometry(QtCore.QRect(60, 510, 46, 31))
        self.labelLevel9.setObjectName(_fromUtf8("labelLevel9"))
        self.labelLevel5 = QtGui.QLabel(mainWindow)
        self.labelLevel5.setGeometry(QtCore.QRect(60, 270, 46, 13))
        self.labelLevel5.setObjectName(_fromUtf8("labelLevel5"))
        self.verticalSlider = QtGui.QSlider(mainWindow)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 30, 41, 561))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.verticalSlider.setFont(font)
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.verticalSlider.setTickInterval(1)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.labelLevel6 = QtGui.QLabel(mainWindow)
        self.labelLevel6.setGeometry(QtCore.QRect(60, 330, 46, 21))
        self.labelLevel6.setObjectName(_fromUtf8("labelLevel6"))
        self.labelLevel3 = QtGui.QLabel(mainWindow)
        self.labelLevel3.setGeometry(QtCore.QRect(60, 140, 46, 31))
        self.labelLevel3.setObjectName(_fromUtf8("labelLevel3"))
        self.listSets = QtGui.QListWidget(mainWindow)
        self.listSets.setGeometry(QtCore.QRect(100, 20, 256, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listSets.setFont(font)
        self.listSets.setAlternatingRowColors(True)
        self.listSets.setViewMode(QtGui.QListView.ListMode)
        self.listSets.setObjectName(_fromUtf8("listSets"))
        item = QtGui.QListWidgetItem()
        self.listSets.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listSets.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listSets.addItem(item)
        self.labelLevel1 = QtGui.QLabel(mainWindow)
        self.labelLevel1.setGeometry(QtCore.QRect(60, 30, 46, 20))
        self.labelLevel1.setObjectName(_fromUtf8("labelLevel1"))
        self.labelLevel = QtGui.QLabel(mainWindow)
        self.labelLevel.setGeometry(QtCore.QRect(20, 10, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLevel.setFont(font)
        self.labelLevel.setObjectName(_fromUtf8("labelLevel"))
        self.btnRemoveSet = QtGui.QPushButton(mainWindow)
        self.btnRemoveSet.setGeometry(QtCore.QRect(260, 310, 41, 41))
        self.btnRemoveSet.setText(_fromUtf8(""))
        self.btnRemoveSet.setIcon(icon)
        self.btnRemoveSet.setIconSize(QtCore.QSize(32, 32))
        self.btnRemoveSet.setObjectName(_fromUtf8("btnRemoveSet"))

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Customization - Sifteos for Dyslexia", None))
        self.btnSave.setText(_translate("mainWindow", "Save Settings File", None))
        self.btnLoad.setText(_translate("mainWindow", "Load Settings File", None))
        self.btnInstall.setText(_translate("mainWindow", "Install on Sifteos", None))
        self.labelLevel4.setText(_translate("mainWindow", "4", None))
        self.labelLevel8.setText(_translate("mainWindow", "8", None))
        self.labelLevel7.setText(_translate("mainWindow", "7", None))
        self.labelLevel10.setText(_translate("mainWindow", "10", None))
        self.groupBox.setTitle(_translate("mainWindow", "Result Weight Settings", None))
        self.lblFailedAttempts.setText(_translate("mainWindow", "Failed Attempts:", None))
        self.lblHintsRequested.setText(_translate("mainWindow", "Hints Requested:", None))
        self.lblTime.setText(_translate("mainWindow", "Time:", None))
        self.lblAttempts.setText(_translate("mainWindow", "50%", None))
        self.lblHints.setText(_translate("mainWindow", "50%", None))
        self.lblTimeValue.setText(_translate("mainWindow", "50%", None))
        self.btnSetGoal.setText(_translate("mainWindow", "Set Goal", None))
        __sortingEnabled = self.listPhonemes.isSortingEnabled()
        self.listPhonemes.setSortingEnabled(False)
        item = self.listPhonemes.item(0)
        item.setText(_translate("mainWindow", "Phoneme 1", None))
        item = self.listPhonemes.item(1)
        item.setText(_translate("mainWindow", "Phoneme 2", None))
        item = self.listPhonemes.item(2)
        item.setText(_translate("mainWindow", "Phoneme 3", None))
        self.listPhonemes.setSortingEnabled(__sortingEnabled)
        self.soundsGroup.setTitle(_translate("mainWindow", "Phoneme Sound", None))
        self.btnA.setText(_translate("mainWindow", "a", None))
        self.btnO.setText(_translate("mainWindow", "o", None))
        self.btnEU.setText(_translate("mainWindow", "eu", None))
        self.btnE_grave.setText(_translate("mainWindow", "è", None))
        self.btnE_acute.setText(_translate("mainWindow", "é", None))
        self.btnE.setText(_translate("mainWindow", "e", None))
        self.btnI.setText(_translate("mainWindow", "i", None))
        self.btnU.setText(_translate("mainWindow", "u", None))
        self.btnOU.setText(_translate("mainWindow", "ou", None))
        self.btnAN.setText(_translate("mainWindow", "an", None))
        self.btnON.setText(_translate("mainWindow", "on", None))
        self.btnUN.setText(_translate("mainWindow", "un", None))
        self.btnIN.setText(_translate("mainWindow", "in", None))
        self.btnILL.setText(_translate("mainWindow", "ill/y", None))
        self.btnUI.setText(_translate("mainWindow", "ui", None))
        self.btnOI.setText(_translate("mainWindow", "oi/w", None))
        self.btnP.setText(_translate("mainWindow", "p", None))
        self.btnB.setText(_translate("mainWindow", "b", None))
        self.btnF.setText(_translate("mainWindow", "f", None))
        self.btnV.setText(_translate("mainWindow", "v", None))
        self.btnM.setText(_translate("mainWindow", "m", None))
        self.btnR.setText(_translate("mainWindow", "r", None))
        self.btnT.setText(_translate("mainWindow", "t", None))
        self.btnD.setText(_translate("mainWindow", "d", None))
        self.btnS.setText(_translate("mainWindow", "s", None))
        self.btnZ.setText(_translate("mainWindow", "z", None))
        self.btnN.setText(_translate("mainWindow", "n", None))
        self.btnL.setText(_translate("mainWindow", "l", None))
        self.btnK.setText(_translate("mainWindow", "k", None))
        self.btnG.setText(_translate("mainWindow", "g", None))
        self.btnCH.setText(_translate("mainWindow", "ch", None))
        self.btnJ.setText(_translate("mainWindow", "j", None))
        self.btnGN.setText(_translate("mainWindow", "gn", None))
        self.btnModifySounds.setText(_translate("mainWindow", "Modify Sound Files", None))
        self.btnCustom.setText(_translate("mainWindow", "Custom", None))
        self.imageGroup.setTitle(_translate("mainWindow", "Phoneme Image", None))
        self.btnLoadImage.setText(_translate("mainWindow", "Load Image", None))
        self.labelLevel2.setText(_translate("mainWindow", "2", None))
        self.labelLevel9.setText(_translate("mainWindow", "9", None))
        self.labelLevel5.setText(_translate("mainWindow", "5", None))
        self.labelLevel6.setText(_translate("mainWindow", "6", None))
        self.labelLevel3.setText(_translate("mainWindow", "3", None))
        __sortingEnabled = self.listSets.isSortingEnabled()
        self.listSets.setSortingEnabled(False)
        item = self.listSets.item(0)
        item.setText(_translate("mainWindow", "Set 1", None))
        item = self.listSets.item(1)
        item.setText(_translate("mainWindow", "Set 2", None))
        item = self.listSets.item(2)
        item.setText(_translate("mainWindow", "Set 3", None))
        self.listSets.setSortingEnabled(__sortingEnabled)
        self.labelLevel1.setText(_translate("mainWindow", "1", None))
        self.labelLevel.setText(_translate("mainWindow", "Level", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QDialog()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

