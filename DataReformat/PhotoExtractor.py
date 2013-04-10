# -*- coding: utf-8 -*-
"""
This script changes the saved file system from images saved
within word documents to a file system with folders and images

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys, os, shutil, tarfile, ntpath, zipfile, re, codecs, xml.etree.ElementTree as ET
from msvcrt import getch
from PIL import Image, ImageOps, ImageDraw, ImageFont

print ("Photo Extraction Script")

path = os.getcwd()
filename = ""
NonValidChars = "\\/:*?\"<>|0123456789"

def makeValidFileName(imageTitle):
    validFileName = ''.join(c for c in imageTitle if not c in NonValidChars)
    return validFileName

def removePronounciation(text):
    tempText = re.sub(r'\/.*?\/', '', text)
    return tempText

def extractFilesFromDoc(files, root):
    global filename
    filename, extension = os.path.splitext(files)
    files = os.path.join(root, files)
    filename = os.path.join(root, filename)
    if not os.path.exists(filename):
        os.makedirs(filename)
    zipFileName = filename + ".zip"
    shutil.copyfile(files, zipFileName)
    shutil.move(files, filename)
    myzip = zipfile.ZipFile(zipFileName, 'a')
    hasImages = False
    myzip.extract("word/document.xml", filename)
    for imageName in myzip.namelist():
        if imageName.startswith("word/media/"):
            myzip.extract(imageName, filename)
            hasImages = True
    myzip.close()
    os.remove(zipFileName)
    """We're done with the zip file, so we've now deleted it"""
    return hasImages

#processing for the pronounciation sections
def processTextForTitle(text):
    textTemp = text.strip()
    print(textTemp)
    if textTemp.startswith("//"):
        if textTemp.endswith("//"):
            return ''
    return text

def parseXmlToRenameImages(files, rootPath):
    """This is where we're going to be doing the xml parsing"""
    imageNumber = 1
    xmlfile = filename + "/word/document.xml"
    string = open(xmlfile).read()
    string = re.sub(':','', string)
    string = re.sub('\'','', string)
    string = re.sub('\s+',' ', string)
    open(xmlfile, 'w').write(string)
    try:
        #tree = ET.fromstring(string)
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for sectionElement in tree.iter('wtc'):
            wtcIter = 0
            imageTitle = ''
            for possibleSection in sectionElement.iter("wt"):
                try:
                    #imageTitle = ''.join(e for e in possibleSection.text if e.isalnum())
                    #imageTitle = imageTitle.join(possibleSection.text.split())
                    imageTitle = imageTitle + possibleSection.text #processTextForTitle(possibleSection.text)
                except UnicodeEncodeError:
                    imageTitle = imageTitle + str(wtcIter)
                    wtcIter = wtcIter + 1
            for sectionWithDrawing in sectionElement.iter('wdrawing'):
                #lets do some text parsing before we go about using the imageTitle
                imageTitle = removePronounciation(imageTitle)
                imageTitle = makeValidFileName(imageTitle)
                imageTitle = imageTitle.strip()
                oldImageTitle = filename + "/word/media/image" + str(imageNumber)
                for images in os.listdir(filename + "/word/media/"):
                    oldImageTitleTemp, extensionTemp = os.path.splitext(images)
                    if oldImageTitleTemp == "image" + str(imageNumber):
                        shutil.move(filename + "/word/media/" + images, os.path.join(filename, imageTitle) + extensionTemp)
                        processImageForSifte(rootPath, filename, imageTitle, extensionTemp)
                        break
                imageNumber = imageNumber + 1
                #Finished with the XML Parsing
    except ET.ParseError:
        #do nothing
        pass
        
"""- for every file in the directory that ends with a '.docx'
make a directory for that file and place both that file, and
a cope of that file (copy is made as a zip file) in the newly
created directory-"""
def convertFilesRecursively():
    global path                
    logFile = open("log.txt", "w")
    for r,d,f in os.walk(path):
        for files in f:
            #This is where we actually create the .zip files
            if files.endswith(".docx"):
                try:
                    print("extracting file: " + os.path.join(r, files))
                    if extractFilesFromDoc(files, r):
                        parseXmlToRenameImages(files, r)
                        #Done with the 'word' directory, remove it
                        shutil.rmtree(filename + "/word")
                except UnicodeEncodeError:
                    #will have to change this back to r
                    print ("Error with converting file: " + files, file=logFile)
                except OSError:
                    #will have to change this back to r
                    print ("Error with converting file: " + files, file=logFile)

def ExtractPhotos():
    print("PhotoExtractor should only be run once for each folder structure and can increase disk usage. Continue? (y/n)")
    while True:
        char = getch()
        if char.lower() == 'y':
            convertFilesRecursively()
        elif char.lower() == 'n':
            break

def extractPilLibrary():
    if not os.path.exists("Imaging-1.1.7"):
        try:
            print('Starting extraction of PIL library')
            tar = tarfile.open('Imaging-1.1.7.tar.gz', 'r:gz')
            for item in tar:
                tar.extract(item)
            print('Finished extracting PIL library')
        except:
            pass
    else:
        print("PIL 1.1.7 library already exists")

def removeTransparency(image):
    background = Image.new("RGB", image.size, (255, 255, 255))
    #background.paste(image, mask=image.split()[3])
    return background

def processImageForSifte(rootPath, folderName, imageTitle, extension):
    if not imageTitle == '':
        completeImageName = os.path.join(os.path.join(rootPath, folderName), imageTitle)
        image = Image.open(completeImageName + extension)
        #scale image
        imageWidth, imageHeight = image.size
        ratio = min(128/imageWidth, 98/imageHeight)
        newImageHeight = int(imageHeight*ratio)
        newImageWidth = int(imageWidth*ratio)
        size = newImageWidth, newImageHeight
        image = image.resize(size)
        #image2 = image.thumbnail(size, Image.ANTIALIAS)
        #add white bar to bottom for text
        #image = ImageOps.fit(image, (128, 128), Image.NEAREST, 0, (1.0, 0.0))
        horizontalImageSpacing = int((128-newImageWidth)/2)
        image = image.crop(( -1*horizontalImageSpacing,0,newImageWidth+horizontalImageSpacing,128))
        draw = ImageDraw.Draw(image)
        myFont = ImageFont.truetype("Arial.ttf", 20, encoding="unic")
        textWidth, textHeight = myFont.getsize(imageTitle)
        textHorizontalPosition = 64 - (textWidth/2)
        textVerticalPosition = 98 + (15 - (textHeight/2))
        #myFont = ImageFont.load("timR14.pil")
        #border
        #draw.text((textHorizontalPosition-1, textVerticalPosition), imageTitle, fill='white', font=myFont)
        #draw.text((textHorizontalPosition+1, textVerticalPosition), imageTitle, fill='white', font=myFont)
        #draw.text((textHorizontalPosition, textVerticalPosition-1), imageTitle, fill='white', font=myFont)
        #draw.text((textHorizontalPosition, textVerticalPosition+1), imageTitle, fill='white', font=myFont)
        draw.text((textHorizontalPosition, textVerticalPosition), imageTitle, fill='white', font=myFont)
        #draw.text((10, 103), )
        #convert to png
        #image = removeTransparency(image)
        image = image.convert("RGB")
        image.save(completeImageName + ".png", quality=100)
        #image2.save(completeImageName + "2.png", quality=100)
        #remove old image
        if not extension == ".png":
            os.remove(completeImageName + extension)
        


#extractPilLibrary()
convertFilesRecursively()
"""for r,d,f in os.walk(path):
    for files in f:
        print(files)"""

"""for images in os.listdir(filename + "/word/media/"):
    if not Images.endswith(".png"):
        Image.open(images).save(images, 'png')"""
