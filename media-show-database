#!/usr/bin/python2

import pickle

# functions

def unPickleData(databasePath):

    try:
        database = pickle.load(open(databasePath, "rb"))
    except:
        print "...database not found..."

    return database


def viewDatabase(database):
    for k, v in database.items():
           print v


# ok let's show a database

databasePath = raw_input("What database would you like to see (include full path)?: ")

database = unPickleData(databasePath)

viewDatabase(database)

print "that's it dude. exiting"

      
