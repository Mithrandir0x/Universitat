#
# prova.py
#
# autor: olopezsa13
#

def find_dictionary():
    vocFile = open('vocabulary.txt', 'r')
    vocLines = vocFile.readlines()
    dictionary = {}
    for line in vocLines:
        entry = line.split('\t')[0]
        if not entry in dictionary:
            dictionary[entry] = 1
        else:
            dictionary[entry] = dictionary[entry] + 1
    for item in dictionary.items():
        print item[0], 'is repeated ', item[1], ' times'
    
    return dictionary
