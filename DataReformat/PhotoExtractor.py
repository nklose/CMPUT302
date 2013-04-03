"""
This script changes the saved file system from images saved
within word documents to a file system with folders and images

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

import sys, os, shutil, ntpath, zipfile, re, xml.etree.ElementTree as ET

print ("Photo Extraction Script")

path = os.getcwd()
filename = ""

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

def parseXmlToRenameImages(files, rootPath):
    """This is where we're going to be doing the xml parsing"""
    imageNumber = 1
    imageTitle = None
    xmlfile = filename + "/word/document.xml"
    string = open(xmlfile).read()
    string = re.sub(':','', string)
    open(xmlfile, 'w').write(string)
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    try:
        for sectionElement in root.iter('wtc'):
            wtcIter = 0
            for possibleSection in sectionElement.iter("wt"):
                if wtcIter == 0:
                    #imageTitle = ''.join(e for e in possibleSection.text if e.isalnum())
                    imageTitle = possibleSection.text
                    print (os.path.join(rootPath, imageTitle))
                wtcIter = wtcIter + 1
            for sectionWithDrawing in sectionElement.iter('wdrawing'):
                oldImageTitle = filename + "/word/media/image" + str(imageNumber)
                for images in os.listdir(filename + "/word/media/"):
                    oldImageTitleTemp, extensionTemp = os.path.splitext(images)
                    if oldImageTitleTemp == "image" + str(imageNumber):
                        shutil.move(filename + "/word/media/" + images, filename + "/" + imageTitle + extensionTemp)
                        break
                imageNumber = imageNumber + 1
                """Finished with the XML Parsing"""
    except OSError as e:
        lifeIsMeaningless = 1
        
            
"""- for every file in the directory that ends with a '.docx'
make a directory for that file and place both that file, and
a cope of that file (copy is made as a zip file) in the newly
created directory-"""
def convertFilesRecursively():
    global path
    for r,d,f in os.walk(path):
        for files in f:
            #This is where we actually create the .zip files
            if files.endswith(".docx"):
                if extractFilesFromDoc(files, r):
                    parseXmlToRenameImages(files, r)
                    #Done with the 'word' directory, remove it
                    shutil.rmtree(filename + "/word")

convertFilesRecursively()
"""for r,d,f in os.walk(path):
    for files in f:
        print(files)"""

"""for images in os.listdir(filename + "/word/media/"):
    if not Images.endswith(".png"):
        Image.open(images).save(images, 'png')"""
