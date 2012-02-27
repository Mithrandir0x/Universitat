#
# p1.py
#
# autor: olopezsa13
#

#
# This method tries to read the file "peliculas100.dat" and
# returns a multi-sized matrix with the film information
# inside the file.
#
# @returns Array The multi-sized matrix containing data of
#     the films inside "peliculas100.dat".
#
def parser():
    # Initialize the root array that will contain each subsequent arrays.
    database = []
    # Read the file in plain-text format.
    filmEntries = readFilmsFile("peliculas100.dat")
    # Iterate over each string of the array, and parse it.
    for entry in filmEntries:
        # Initialize the new entry to insert in the lil' table.
        databaseEntry = []
        # 'entry' is a string that represents all the data about a movie,
        # and all its information is separated by '|'. It is splitted and
        # treated.
        fields = entry.split("|")
        # Iterate over all the fields to find if there are multiple
        # entities inside a field.
        for field in fields:
            # If there's a '&&' inside the string, it will treat as a
            # composed field, and will split the string and append the
            # array in the field.
            # If not, it will append the string directly.
            if ( field.find("&&") != -1 ):
                composedField = field.split("&&")
                databaseEntry.append(composedField)
            else:
                databaseEntry.append(field)
        # Append the new entry in the table.
        database.append(databaseEntry)
    return database

#
# Given a string with a path to a file, it returns an array
# with each line of the file as a string.
# 
# On error, it will return an empty array.
#
# @param String filename The path to the file.
# @returns Array An array containing each line of the file as a string
#     item.
#
def readFilmsFile(fileName):
    try:
        f = open(fileName, 'r')
        filmEntries = f.readlines()
        f.close()
        return filmEntries
    except IOError:
        print "Error raised on reading file:", fileName
        return []
