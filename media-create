#!/usr/bin/python2

from sys import argv
import os
import hashlib
import pickle


# various declarations

fileTypes =  ['jpg', 'png', 'mov', 'aae', 'jpg', 'cr2', 'mod', 'moi', 'avi', 'mp4', 'm4v', 'pgi', 'gif', 'avi', 'png', 'tiff', 'mov', 'xmp', 'tif', 'jpeg', 'psd', 'bmp', 'pp3', 'thm']

database = {}

# functions

def rePickleData(database, databasePath):

    pickle.dump(database, open(databasePath, "wb"))

def md5Checksum(filePath):
    """return md5 hash for a given file."""
    
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def updateDatabase(searchPath):

    for root, dirs, files in os.walk(searchPath, topdown=True):
        for name in files:

            filePath = os.path.join(root, name)
            nameSplit = name.split(".")                
            fileExtension = nameSplit[-1]

            if fileExtension.lower() in fileTypes:
                
                if "md5" not in name:

                    fileHash = md5Checksum(filePath)

                    if fileHash in database:
                        if filePath not in database[fileHash]:
                            database[fileHash].append(filePath)

                    else:
                        database[fileHash] = [filePath]

                else:

                    nameSplit = name.split(".")
                    fileHash = nameSplit[0][-32:]

                    if fileHash in database:
                        if filePath not in database[fileHash]:
                            database[fileHash].append(filePath)
                    else:
                        database[fileHash] = [filePath]

    return database



# ok time to run something

pathToFiles = raw_input("please give a complete path to the files we are cataloging: ")

databaseName = raw_input("please give a filename for the database we are creating\n recommended databaseCatalog or databaseComparison\n: ")

print "cataloging files..."

updateDatabase(pathToFiles)

print "database updated!"
    
rePickleData(database, databaseName)

print "database saved! success. %s is all good. exiting..." % databaseName
