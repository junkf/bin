#!/usr/bin/python2

import os
import pickle
import shutil

# functions

def unPickleData(databasePath):

    try:
        database = pickle.load(open(databasePath, "rb"))
    except:
        print "...database not found..."

    return database


def copyFromDatabase(database, destinationPath):

        for key, value in database.items():
            source = value[0][0]
            print "copying ", source, " to ", destinationPath
            shutil.copy(source, destinationPath)

 # ok let's roll

databasePath = raw_input("give the name of the database you want to copy from (probably databaseUnique) with full path\n: ")

database = unPickleData(databasePath)

destinationPath = raw_input("where would you like those files to go (give full path)\n:")

raw_input("about to copy files from %s ... to %s hit a key..." % (databasePath, destinationPath))

copyFromDatabase(database, destinationPath)

print "no exceptions. Guess we're cool. exiting cleanly now."
 
