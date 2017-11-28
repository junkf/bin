#! /usr/bin/python2

import os

# delcarations

junk = ["[", "]", "-", "  ", "_"]
cwd = os.getcwd()

filenames = os.listdir(cwd)

for filename in filenames:

    print "\n", "*"*35
    
    tempname = filename.split('.')

    if len(tempname) > 1:
        extension = tempname.pop()

        temptempname = ' '.join(tempname)
        
        filetuple = (temptempname, extension)

        print "filename = ", filename
        print "temptempname = ", temptempname
        print "extension = ", extension
        print "filetuple = ", filetuple

    else:
        filetuple = (filename, "Null")
        
        print "filename = ", filename
        print "This file doesn't seem to have an extension."
        print "filetuple = ", filetuple

#    raw_input("Hit ctrl-c if this doesn't look right, otherwise, let's go!")

    lowername = filetuple[0].lower()

    for j in junk:
        if j in lowername:
            lowername = lowername.replace(j, ' ')

            print "\n***FOUND --> %s <-- therefore:" % j, 
            print filename, " --> ", lowername, "\n"
            print "AND new filename is: ", lowername + "." + filetuple[1]
            
        else:
            print "NO --> '%s' <--" % j,
    
#    os.rename(filename, newname)


