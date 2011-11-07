#
# exercici5.py
#
# autor: olopezsa13
#

import math
import time

# Metode iteratiu, molt mes eficient i sense el problema de profunditat
def iterativeFib(N):
    f0 = 0
    f1 = 1
    i = 0
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        while i < N:
            f0, f1 = f1, f0 + f1
            i = i + 1
    return f0

def fib1():
    n = input('Escriu per a quin terme "n" vols que calculi fibonacci: ')
    tStart = time.clock()
    fibRes = iterativeFib(n)
    print 'Temps del calcul:', time.clock() - tStart
    print 'Fibonacci(',n,') =', fibRes

def realMcd(m, n):
    mod = m % n
    if mod == 0:
        return n
    else:
        return realMcd(n, mod)

def mcd():
    m = input('Escriu el terme m: ')
    n = input('Escriu el terme n: ')
    print realMcd(m, n)

# S'utilitzen list comprehensions
# 10000000 ~14.7s | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.2
def listComprehenSieve(A, N):
    sqrtN = math.sqrt(N)
    [ setAiMinusOne(A, j) for i in xrange(A.index(int(sqrtN + 1)) + 1) for j in xrange(i, len(A), A[i]) if A[i] != A[j] and A[j] % A[i] == 0 ]

def setAiMinusOne(A, i):
    A[i] = -1

def cleanEraList(A):
    return [ A[i] for i in range(0, len(A)) if A[i] != -1 ]

def realEra(N):
    A = [i for i in range(2, N + 1)]
    listComprehenSieve(A, N)
    return A

def era1():
    N = input('Escriu el terme n: ')
    tStart = time.clock()
    primeList = realEra(N)
    primeList = cleanEraList(primeList)
    print time.clock() - tStart
    print primeList

# Es triguen 17.19 segons a completar aquesta funcio en un Mac Mini amb un 
# Intel P8600 - Python 2.6.2 - Snow Leopard 10.6.8
def era2():
    tStart = time.clock()
    primeList = realEra(10000000)
    primeList = cleanEraList(primeList)
    print time.clock() - tStart
    print len(primeList)

def factorp():
    n = input('Introdueix el nombre a factoritzar: ')
    if n == 1:
        return [1]
    tStart = time.clock()
    A = realEra(n)
    A = cleanEraList(A)
    iPrime = 0
    factorList = []
    while n != 1:
        if n % A[iPrime] == 0:
            factorList.append(A[iPrime])
            n = n / A[iPrime]
        else:
            iPrime = iPrime + 1
    print time.clock() - tStart
    print factorList

def fermatp():
    n = input('Escriu un valor n: ')
    aValues = [2, 3, 5]
    tStart = time.clock()
    for a in aValues:
        if (a ** (n - 1)) % n == 1:
            print 'Per n =', n, ' i a =', a, ' es podria considerar un nombre prim.'
        else:
            print 'Per n =', n, ' i a =', a, ' es un nombre compost.'
    print time.clock() - tStart

