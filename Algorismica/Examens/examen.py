#
# examen.py
#
# autor: olopezsa13
#

import math
import time

def levenshtein(text, pattern):
    text = text.rstrip()
    pattern = pattern.rstrip()
    lnText = len(text) + 1
    lnPattern = len(pattern) + 1
    distanceMatrix = [[0] * lnPattern for x in range(lnText)]
    for j in range(lnPattern): distanceMatrix[0][j] = j
    for i in xrange(1, lnText):
        for j in xrange(1, lnPattern):
            deletion = distanceMatrix[i-1][j] + 1
            insertion = distanceMatrix[i][j-1] + 1
            substitution = distanceMatrix[i-1][j-1]
            if text[i-1] != pattern[j-1]:
                substitution += 2
            distanceMatrix[i][j] = min(insertion, deletion, substitution)
    return distanceMatrix

def vector3(i, j, v):
    return { 'i': i, 'j': j, 'v': v }

def perV(v):
    return v['v']

def trobarCostEdicioMinim(md):
    ultimaFila = len(md[0]) - 1
    costEdicio = vector3(-1, -1, float('inf'))
    for i in range(len(md) - 1, -1, -1):
        if md[i][ultimaFila] <= costEdicio['v']:
            costEdicio['v'] = md[i][ultimaFila]
            costEdicio['i'] = i
            costEdicio['j'] = ultimaFila
    return costEdicio

def reconstruirCami(md, ultimaEdicio):
    cami = []
    cami.append(ultimaEdicio)
    i = ultimaEdicio['i']
    j = ultimaEdicio['j']
    while j > 0:
         llistaAdjacents = [ 
             vector3(i    , j - 1, md[i][j-1]),
             vector3(i - 1, j - 1, md[i - 1][j - 1]),
             vector3(i - 1, j    , md[i - 1][j]) ]
         part = min(llistaAdjacents, key=perV)
         cami.append(part)
         i = part['i']
         j = part['j']
    return cami

def llegirBinari(nomFitxer, k):
    try:
        f = open(nomFitxer, 'r')
        liniesBinari = f.readlines()
        print liniesBinari[0]
        f.close()
        nFragment = ( len(liniesBinari[0]) / k ) + 1
        return [ liniesBinari[0][i:i + nFragment] for i in range(0, len(liniesBinari[0]), nFragment) ]
    except IOError:
        print "No s'ha trobat el fitxer demanat"
        return []

def search(patro, k):
    print 'The pattern', patro, 'in:'
    cadenes = llegirBinari('text.txt', k)
    for linia, cadena in enumerate(cadenes):
        matriu = levenshtein(cadena, patro)
        cm = trobarCostEdicioMinim(matriu)
        camiEdicio = reconstruirCami(matriu, cm)
        print linia + 1,': ', cadena[camiEdicio[len(camiEdicio) - 1]['i'] - 1:camiEdicio[0]['i']]

def Sieve(N):
    A = [i for i in range(2, N + 1)]
    listComprehenSieve(A, N)
    return A

def listComprehenSieve(A, N):
    sqrtN = math.sqrt(N)
    [ setAiMinusOne(A, j) for i in xrange(A.index(int(sqrtN + 1)) + 1) for j in xrange(i, len(A), A[i]) if A[i] != A[j] and A[j] % A[i] == 0 ]

def setAiMinusOne(A, i):
    A[i] = -1

def search_prim_fact(k, m):
    tStart = time.time()
    llistaPrims = Sieve(k)
    for p in llistaPrims:
        if p != -1:
            factP = math.factorial(p)
            if factP < m:
                print 'Prim', p, 'fact', factP
    print 'The program spends', ( time.time() - tStart ) * 1000, 'milliseconds'
    