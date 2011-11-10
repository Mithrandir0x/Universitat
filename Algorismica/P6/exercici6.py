#
# exercici6.py
#
# autor: olopezsa13
#

def levenshtein(text, pattern):
    lnText = len(text) + 1
    lnPattern = len(pattern) + 1
    distanceMatrix = [[0] * lnPattern for x in range(lnText)]
    for j in range(lnPattern): distanceMatrix[0][j] = j
    for i in xrange(1, lnText):
        for j in range(1, lnPattern):
            deletion = distanceMatrix[i-1][j] + 2
            insertion = distanceMatrix[i][j-1] + 2
            substitution = distanceMatrix[i-1][j-1]
            if text[i-1] != pattern[j-1]:
                substitution += 1
            distanceMatrix[i][j] = min(insertion, deletion, substitution)
    return distanceMatrix

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
    for cadena in cadenes:
        for fragment in cromosoma2:
            dm = levenshtein(fragment, cadena)
    matriu = levenshtein('C ABBA C', 'DDD')
    print matriu

cercaGenetica()

