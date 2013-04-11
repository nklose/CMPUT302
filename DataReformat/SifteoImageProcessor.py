import sys, os
import pickle
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow
from os.path import basename
from PIL import Image, ImageOps, ImageDraw, ImageFont

NonValidChars = "\\/:*?\"<>|0123456789"

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Force consistent theme and font size
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setStyleSheet("font-size: 11pt")

        # Disable resizing
        self.setFixedSize(self.size())

        #######################################################
        # Interface Object Connections                        #
        #######################################################
        itemClicked = QtCore.SIGNAL("itemClicked(QListWidgetItem *)")
        clicked = QtCore.SIGNAL("clicked()")

        ## Buttons
        QtCore.QObject.connect(self.ui.pushButton_convert, clicked, self.convertImage)
        QtCore.QObject.connect(self.ui.pushButton_loadImage, clicked, self.loadImage)

    def loadImage(self):
        imageName = str(QtGui.QFileDialog.getOpenFileName())
        self.ui.label_imageFile = imageName

    def convertImage(self):
        imageName = self.ui.label_imageFile
        imageTitle = self.ui.lineEdit_title.text()
        if not imageTitle == '':
            filename, extension = os.path.splitext(imageName)
            directory, file = os.path.split(filename)
            image = Image.open(imageName)
            #scale image
            imageWidth, imageHeight = image.size
            ratio = min(128/imageWidth, 98/imageHeight)
            newImageHeight = int(imageHeight*ratio)
            newImageWidth = int(imageWidth*ratio)
            size = newImageWidth, newImageHeight
            image = image.resize(size)
            #add white bar to bottom for text
            horizontalImageSpacing = int((128-newImageWidth)/2)
            image = image.crop(( -1*horizontalImageSpacing,0,newImageWidth+horizontalImageSpacing,128))
            draw = ImageDraw.Draw(image)
            myFont = ImageFont.truetype("Arial.ttf", 20, encoding="unic")
            textWidth, textHeight = myFont.getsize(imageTitle)
            textHorizontalPosition = 64 - (textWidth/2)
            textVerticalPosition = 98 + (15 - (textHeight/2))
            draw.text((textHorizontalPosition, textVerticalPosition), imageTitle, fill="white", font=myFont)
            image = image.convert("RGB")
            #convert to png
            validFileName = ''.join(c for c in imageTitle if not c in NonValidChars)
            image.save(os.path.join(directory, validFileName) + ".png", quality=100)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
