#!/usr/bin/python2

import os
import hashlib
import PIL
from PIL import Image
import shutil

# various declarations

fileTypes =  ['jpg', 'png', 'mov', 'aae', 'jpg', 'cr2', 'mod', 'moi', 'avi', 'mp4', 'm4v', 'pgi', 'gif', 'avi', 'png', 'tiff', 'mov', 'xmp', 'tif', 'jpeg', 'psd', 'bmp', 'pp3', 'thm']

# functions


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

def renameWithHash(path):
    """walk directory tree, rename files with md5 checksum."""

    print "starting now..."

    for (path, dirs, files) in os.walk(path):
        for name in files:

	    print "name"

            if "md5" not in name:

                nameSplit = name.split(".")
                oldName = os.path.join(path, name)
                newName = os.path.join(path, (nameSplit[0] + "-md5-" + md5Checksum(os.path.join(path, name)) + "." + nameSplit[-1]))
                print "renaming file ", oldName, " to ", newName, "\n"
                os.rename(oldName, newName)

            else:

                print "blurg"

def renameWithDate(path):
    """walk directory tree, add original date from exif to filename."""

    for (path, dirs, files) in os.walk(path):
        for name in files:
            
            nameSplit = name.split(".")
            originalName = os.path.join(path, name)

            if nameSplit[-1].lower() == "jpg":
                
                if "Oringinal-Date" not in name:

                    try:

                        image = PIL.Image.open(originalName)
                        exifData = image._getexif()
                        exifOriginalDate = str(exifData[36867][0:4])
#                        print str(exifData[36867])
                        newName = os.path.join(path, exifOriginalDate + "-Original-Date-" + name)
                        print "renaming file ", originalName, " to ", newName, "\n"
                        os.rename(originalName, newName)
   
                    except:
                        print "oops, there was some kind of exception here."

            else:
                print "for ", name, "\nsorry, I can only rename jpegs right now!\n"


# OK let's run this thing!

print "renaming media files with md5 hash and dates if available.... ctl-c to bail..."

path = raw_input("give path to start our walk: ")

renameWithHash(path)

renameWithDate(path)

print "done."
