#
# exercici6.py
#
# autor: olopezsa13
#

def levenshtein(first, second):
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    lFirst = len(first) + 1
    lSecond = len(second) + 1
    distanceMatrix = [[0] * lSecond for x in range(lFirst)]
    for j in range(lSecond): distanceMatrix[0][j] = j
    for i in xrange(1, lFirst):
        for j in range(1, lSecond):
            deletion = distanceMatrix[i-1][j] + 1
            insertion = distanceMatrix[i][j-1] + 1
            substitution = distanceMatrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
                distanceMatrix[i][j] = min(insertion, deletion, substitution)
    return distanceMatrix[lFirst-1][lSecond-1]

def llegirCromosoma(fitxer):
    try:
        f = open(fitxer, 'r')
        liniesCromosoma = f.readLines()
        f.close()
        return liniesCromosoma
    except IOError:
        print "No s'ha trobat el fitxer demanat"
        return []

def cercaGenetica():
    cadenes = [ 
        'AGATACATTAGACAATAGAGATGTGGTC',
        'GTCAGTCTGGCCTTGCCATTGGTGCCACCA',
        'TACCGAGAAGCTGGATTACAGCATGTACCATCAT' ]
    cromosoma2 = llegirCromosoma('HUMAN-DNA.txt')


