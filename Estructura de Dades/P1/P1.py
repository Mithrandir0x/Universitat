#
# P1.py
#
# autor: olopezsa13
#

def parser():
	database = []
	filmEntries = readFilmsFile("peliculas100.dat")
	for entry in filmEntries:
		databaseEntry = []
		fields = entry.split("|")
		for field in fields:
			if ( field.find("&&") ):
				composedField = field.split("&&")
				databaseEntry.append(composedField)
			else:
				databaseEntry.append(field)
		database.append(databaseEntry)
	return database

def readFilmsFile(fileName):
    try:
        f = open(fileName, 'r')
        filmEntries = f.readlines()
        f.close()
        return filmEntries
    except IOError:
        print "Error raised on reading file:", fileName
        return []
