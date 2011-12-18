# -*- coding: iso-8859-15 -*-

import cProfile
import math
import random
import time

__NCALLS__ = 0

# Definim la funcio d'avaluacio.
def punt(r, start, length):
    # Transformem els bits en un valor real x a l'interval [start, start+length]
    sum = 0.0
    pow2 = 1
    for i in xrange(len(r)):
        sum += r[i] * pow2
        pow2 *= 2
    x = start + sum * ( length / ( 2.0 ** (len(r))-1.0 ) )
    return x

def cost(r):
    # Avaluem el cromosoma x
    global __NCALLS__
    __NCALLS__ += 1
    x = punt(r, -1.0, 3.0)
    y = x * math.sin(10*math.pi*(x))+1.0
    return y

def cost2(v):
    global __NCALLS__
    __NCALLS__ += 1
    x = punt(v[0], -6.0, 12.0)
    y = punt(v[1], -6.0, 12.0)
    z = 200.0 - ( ( x ** 2.0 + y - 11.0 ) ** 2.0 ) - ( ( x + y ** 2.0 - 7.0 ) ** 2.0 )
    return z

# Definim el creuament
def creuament(r1, r2):
    i = random.randint(1, len(r1)-2)
    return r1[:i]+r2[i:], r2[:i]+r1[i:]

# Definim la mutacio amb probabilitat mutprob per cada bit
def mutacio(r, mutprob):
    for i in range(len(r)):
        if random.random() < mutprob: 
            if r[i] == 0:
                r[i]=1
            else:
                r[i]=0
    return r

# Creem la població inicial
def initpop(n, long):
    # Generem una poblacio de n cromosomes de longitud long. 
    pop = [ [0] * long for x in range(n) ]
    for i in range(n):
        for j in range(long):
            if random.random() > 0.5:
                pop[i][j] += 1 
    return pop

def initpop2(n, long):
    population = [ [[0] * long, [0] * long] for x in range(n) ]
    for i in range(n):
        for j in range(long):
            if random.random() > 0.5:
                population[i][0][j] += 1
            if random.random() > 0.5:
                population[i][1][j] += 1
    return population

# Definim el proces de seleccio estandard
def seleccio_std(pop, cost, start=0):
    popsize = len(pop)
    # Calculem el valor minim de la funcio d'avaluacio   
    c = [ cost(v) for v in pop[start:] ]
    minim = min(c)
    # Normalitzem els valors de manera que el pitjor 
    # individu tingui un valor 0.01
    if minim < 0.0: 
        for i in range(len(c)): 
            c[i] = c[i] + abs(minim) + 0.01
    else: 
        for i in range(len(c)): 
            c[i] = c[i] - minim + 0.01
    # Calculem la suma de tots els valors de la funcio d'avaluacio
    sum = 0.0
    for i in range(len(c)):
        sum = sum + c[i]
    # Triem l'individu de forma proporcional al seu valor d'adaptacio 
    ran = random.random() * sum
    i = 0
    sum2 = c[0]
    while ran > sum2: 
        i += 1
        sum2 = sum2 + c[i]
    # Retornem l'individu seleccionat
    return i + start

# Definim l'algorisme genètic 
# Restriccio: popsize ha d'esser un nombre parell
def genetic(cost, cromsize=22, popsize=50, mutprob=0.01, maxiter=150):
    global __NCALLS__
    __NCALLS__ = 0
    # Generem la població inicial
    pop = initpop(popsize, cromsize)
    tStart = time.time()
    # Iterem fins al nombre de generacions
    for cont in range(maxiter):
        # Avaluem la generacio i l'ordenem
        scores = [ (cost(xbin), xbin) for xbin in pop ]
        scores.sort(reverse=True)
        ranked = [ xbin for (fx, xbin) in scores ]
        # Afegim els dos millors cromosomes a la següent generacío
        newpop = [0] * popsize
        newpop[0],newpop[1] = ranked[0],ranked[1]
        # Seleccionem les parelles 
        for i in range(0, popsize, 2):
            ind1 = seleccio_std(ranked, cost, i)
            ranked[i],ranked[ind1] = ranked[ind1],ranked[i]
            ind2 = seleccio_std(ranked, cost, i+1)
            ranked[i+1],ranked[ind2] = ranked[ind2],ranked[i+1]
        # Creuem les parelles i generem els fills
        new = [0] * popsize
        for i in range(0, popsize, 2): 
            new[i],new[i+1] = creuament(ranked[i], ranked[i+1])
        # Mutem
        mut = [0] * popsize
        for i in range(popsize):
            mut[i] = mutacio(new[i], mutprob)
        # Afegim els pares (excepte els dos millors) a la generació
        mut = mut + ranked[2:]
        # Seleccionem la resta d'individus per la següent generació
        for i in range(2, popsize):
            newpop[i] = mut[seleccio_std(mut, cost, i)]
        pop = newpop
    tEnd = time.time()
    print "f(x):", scores[0][0],
    print "x:", punt(scores[0][1], -1.0, 3.0)
    print 't:', tEnd - tStart
    print 'nCalls:', __NCALLS__

def genetic2(cost, cromsize=22, popsize=50, mutprob=0.01, maxiter=200):
    global __NCALLS__
    __NCALLS__ = 0
    population = initpop2(popsize, cromsize)
    tStart = time.time()
    for iteration in range(maxiter):
        scores = [ [ cost(pbin), pbin ] for pbin in population ]
        scores.sort(reverse=True)
        ranked = [ pbin for ( number, pbin ) in scores ]
        newpop = [ [ [0] * cromsize , [0] * cromsize ] ] * popsize
        newpop[0], newpop[1] = ranked[0], ranked[1]
        for i in range(0, popsize, 2):
            mare = seleccio_std(ranked, cost, i)
            ranked[i], ranked[mare] = ranked[mare], ranked[i]
            pare = seleccio_std(ranked, cost, i+1)
            ranked[i+1], ranked[pare] = ranked[pare], ranked[i+1]
        new = [ [ [0] * cromsize , [0] * cromsize ] ] * popsize
        for i in range(0, popsize, 2):
            new[i][0], new[i+1][0] = creuament(ranked[i][0], ranked[i+1][0])
            new[i][1], new[i+1][1] = creuament(ranked[i][1], ranked[i+1][1])
        mut = [ [ [0] * cromsize , [0] * cromsize ] ] * popsize
        for i in range(2, popsize):
            newpop[i] = mutacio(new[i][0], mutprob)
            newpop[i] = mutacio(new[i][1], mutprob)
        mut += ranked[2:]
        for i in range(2, popsize):
            newpop[i] = mut[seleccio_std(mut, cost, i)]
        pop = newpop
    tEnd = time.time()
    print "f(x,y):", scores[0][0]
    print "x:", punt(scores[0][1][0], -6.0, 12.0),
    print 'y:', punt(scores[0][1][1], -6.0, 12.0)
    print 't:', tEnd - tStart
    print 'nCalls:', __NCALLS__

