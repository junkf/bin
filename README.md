# bin

#This is the readme file for kind of windy / bin

This repository exists to synchronize useful utilities across my computers.

created on github November 27, 2017

This November 2017 fork of the longstanding python media project gets rid of the menu concept and instead provides a collection of tools.

Some useful conventions:

databaseCatalog, databaseComparison, databaseUnique, databaseDuplicate.


Tools:

rename

	This asks for a path and renames media files in this path with md5 hash and date if available.

create

	This asks for a path and a database name (with full path). It catalogs media files in that path.

compare

	This asks for two databases, compares their contents, and creates databaseUnique and databaseDuplicate at another location.

copy

        This asks for a database (with full path) and a destination (with full path). It copies files to the destination.

