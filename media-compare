#!/usr/bin/python2

import os
import hashlib
import pickle
import PIL
from PIL import Image
import shutil

# various declarations

def unPickleData(databasePath):

    try:
        database = pickle.load(open(databasePath, "rb"))
    except:
        print "...database not found..."

    return database


def rePickleData(databaseName, databasePath):

    pickle.dump(databaseName, open(databasePath, "wb"))

def compareDatabases(databaseMedia, databaseCompare):
    n = 0
    u = 0
    d = 0
    databaseDuplicate = {}
    databaseUnique = {}

    for key, value in databaseCompare.items():

        n += 1
        
        if key in databaseMedia:
            d += 1 
            databaseDuplicate[key] = [value]
#            print "adding ", key,  " to duplicate database\n i.e. file: ", str(value), "\n that's dupliate file number: ", str(n) )

        else:
            u += 1
            databaseUnique[key] = [value]
#            print("adding ", key,  " to unique database\n i.e. file: ", str(value), "\n that's unique file number: ", str(n)

    print "\n\nResults obtained by comparing the databases:\n"
    print str(u), " unique files. ", str(d), " duplicate files. ", str(n), " total files checked in the comparison database."
    return[databaseUnique, databaseDuplicate]


def viewDatabase(databaseName, databaseLabel):
    userInput = raw_input("would you like to review " + databaseLabel + "? [y/n]: ")
    if userInput != '':
       for k, v in databaseName.items():
           print v
    else:
        print "ok, moving on then..."

# ok let's go

# tell me where the databases are

databaseMediaPickled = raw_input("Please give catalog database name with full path\probably catalogDB\n: ")
databaseComparePickled = raw_input("Please give comparison database name with full path\n probably comparisonDB\n: ")

# unpickle those databases

databaseMedia = unPickleData(databaseMediaPickled)
databaseCompare = unPickleData(databaseComparePickled)

# compare those databases and generate duplicate and unique databases

databaseResults = compareDatabases(databaseMedia, databaseCompare)

databaseUnique = databaseResults[0]
databaseDuplicate = databaseResults[1]

# pickle the new databases

pathToNewPickle = raw_input("where should I pickle the unique and duplicate databases?: ")

rePickleData(databaseUnique, pathToNewPickle + "/databaseUnique")
rePickleData(databaseDuplicate, pathToNewPickle + "/databaseDuplicate")

print "Seems there were no exceptions, so I guess we're cool. exiting"

