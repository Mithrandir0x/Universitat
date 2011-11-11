#
# exercici6.py
#
# autor: olopezsa13
#

# In Soviet Russia, zero divides by you...
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

# Donats tres valors qualsevols, els agrupem en una llista associativa, per
# facilitar l'acces i l'escriptura dels elements.
def vector3(x, y, z):
    return { 'x': x, 'y': y, 'z': z }

# Funcio auxiliar utilitzada per la funcio 'reconstruirCami' per retornar el
# valor de z donada una llista creada pel metode 'vector3'.
def perZ(v):
    return v['z']

# Aquesta funcio s'encarrega de cerca el cost minim possible dins d'una
# matriu de distancies de Levenshtein.
def trobarCostEdicioMinim(md):
    ultimaFila = len(md[0]) - 1
    costEdicio = vector3(-1, -1, float('inf'))
    # Trobem el minim de l'ultima fila de la matriu de distancies
    for i in range(len(md) - 1, -1, -1):
        if md[i][ultimaFila] <= costEdicio['z']:
            costEdicio['z'] = md[i][ultimaFila]
            costEdicio['x'] = i
            costEdicio['y'] = ultimaFila
    return costEdicio

# Aquesta funcio ens permet, donada la posicio dins la matriu de distancies,
# conseguir el cami d'edicio minim.
def reconstruirCami(md, ultimaEdicio):
    cami = []
    cami.append(ultimaEdicio)
    i = ultimaEdicio['x']
    j = ultimaEdicio['y']
    while j > 0:
         # Creem una llista amb els elements adjacents del primer
         # element al que estem accedint per trobar quin es el 
         # valor minim.
         llistaAdjacents = [ 
             vector3(i    , j - 1, md[i][j-1]),
             vector3(i - 1, j - 1, md[i - 1][j - 1]),
             vector3(i - 1, j    , md[i - 1][j]) ]
         part = min(llistaAdjacents, key=perZ)
         cami.append(part)
         i = part['x']
         j = part['y']
    return cami

# Funcio encarregada de llegir i retornar totes les linees del nom de fitxer
# donat. En cas de que no existeixi, es retorna un vector buit.
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
        linia = 0
        costMinim = float('inf')
        camiEdicio = None
        tStart = time.time()
        for liniaActual, fragment in enumerate(cromosoma2):
            matriu = levenshtein(fragment, cadena)
            cm = trobarCostEdicioMinim(matriu)
            if cm['z'] < costMinim:
                costMinim = cm['z']
                camiEdicio = reconstruiCami(matriu, costMinim)
                linia = liniaActual
        tElapsed = time.time() - tStart
        print 'El patro', cadena, 'es troba a la linia', linea, 'posicio', camiEdicio[len(camiEdicio)]['x'], 'del cromosoma 2 huma, i la seva distancia d\'edicio es', camiEdicio[0]['z'],'.'
        print 'El substring del cromosoma huma mes semblant es', cromosoma[linea][camiEdicio[len(camiEdicio) - 1]['x']:camiEdicio[0]['x']]
        print 'El temps de calcul ha estat', tElapsed

