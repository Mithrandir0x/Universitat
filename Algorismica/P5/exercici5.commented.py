#
# exercici5.py
#
# autor: olopezsa13
#

import cProfile
import math
import time

# Metode relativament per definicio, pero tenim el inconvenient que es recursiu
#def realFib(f0, f1, i, n):
#    if n == 0:
#        return f0
#    elif n == 1:
#        return f1
#    elif i == n:
#        return f1 + f0
#    else:
#        return realFib(f1, f0 + f1, i + 1, n)

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
    tStart = time.time()
    fibRes = iterativeFib(n)
    print 'Temps del calcul:', time.time() - tStart,'s'
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

# Solucio per definicio
#  50000  ~0.26s (amb pop) | Intel C2D E8500 (VM Virtual Box) - Ubuntu 11.04 (Natty Narwhal) | Python 2.7.1
#  50000  ~0.53s (amb pop) | Intel C2D E8500 - Windows 7 x64 | Python 2.6.2
#  50000  ~1.21s (amb pop) | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.1
# 100000  ~0.93s (amb pop) | Intel C2D E8500 (VM Virtual Box) - Ubuntu 11.04 (Natty Narwhal) | Python 2.7.1
# 100000 ~16.48s (amb pop) | Intel Atom N270 - Windows 7 x32 | Python 2.7.2
#def recursiveSieve(A, B, N):
#    if A[0] > math.sqrt(N):
#        return
#    else:
#        j = 0
#        prime = A[0]
#        B.append(prime)
#        while j < len(A):
#            if A[j] % prime == 0:
#                A.pop(j)
#            j = j + 1
#        recursiveSieve(A, B, N)

# Solucio iterativa de la definicio donada
#def iterativeSieve(A, B, N):
#    sqrtN = math.sqrt(N)
#    prime = A[0]
#    while prime < sqrtN:
#        B.append(prime)
#        j = 0
#        while j < len(A):
#            if A[j] % prime == 0:
#                A.pop(j)
#            j = j + 1
#        prime = A[0]

# No es fa cap manipulacio d'array
#def iterativeSieve2(A, B, N):
#    sqrtN = math.sqrt(N)
#    lA = len(A)
#    i = 0
#    #c2 = 0
#    #c1 = 0
#    while A[i] < sqrtN:
#        if A[i] != None:
#            B.append(A[i])
#            prime = A[i]
#            j = i
#            while j < lA:
#                if A[j] != None and A[j] % prime == 0:
#                    A[j] = None
#                j = j + 1
#                #c2 = c2 + 1
#        i = i + 1
#        #c1 = c1 + 1
#    #print c1, c2, A, B

# iterativeSieve2 pero amb for's
# 1000000 ~818.7s | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.2
# 1000000 ~748.7s (xrange) | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.2
def iterativeSieve2For(A, B, N):
    sqrtN = math.sqrt(N)
    lA = len(A)
    #c2 = 0
    #c1 = 0
    for i in xrange(A.index(int(sqrtN)) + 1):
        if A[i] != None:
            B.append(A[i])
            prime = A[i]
            for j in xrange(i, lA):
                if A[j] != None and A[j] % prime == 0:
                    A[j] = None
                #c2 = c2 + 1
        #c1 = c1 + 1
    #print c1, c2, A, B

# S'utilitzen list comprehensions
# 10000000 ~14.7s | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.2
def listComprehenSieve(A, N):
    sqrtN = math.sqrt(N)
    [ setAiMinusOne(A, j) for i in xrange(A.index(int(sqrtN + 1)) + 1) for j in xrange(i, len(A), A[i]) if A[i] != A[j] and A[j] % A[i] == 0 ]

def setAiMinusOne(A, i):
    A[i] = -1

def era5():
    N = 10000000
    tStart = time.time()
    A = [i for i in range(2, N + 1)]
    listComprehenSieve(A, N)
    #cleanSieve(A)
    print ( time.time() - tStart ) * 1000000
    #print A

#def era0():
#    N = 100
#    A = [i for i in range(2, N + 1)] # Tots els valors entre 2 i N
#    B = [] # Llista on es guardaran tots els nombres primers
#    tStart = time.time()
#    iterativeSieve2(A, B, N)
#    print ( time.time() - tStart ) * 1000000
#    #print mergeSort(A,B)

#def era3():
#    N = 100
#    A = [i for i in range(2, N + 1)] # Tots els valors entre 2 i N
#    B = [] # Llista on es guardaran tots els nombres primers
#    tStart = time.time()
#    iterativeSieve2For(A, B, N)
#    print ( time.time() - tStart ) * 1000000
#    A = [ A[i] for i in range(0, len(A)) if A[i] != None]
#    print A, B 
#    #print A
#    #print B
#    #print mergeSort(A,B)

#def era4():
#    N = 100
#    A = [ i for i in range(2, N + 1) ]
#    tStart = time.time()
#    B = iterativeSieve3(A, N)
#    print ( time.time() - tStart ) * 1000000
#    print B

def realEra(N):
    tStart = time.time()
    A = [i for i in range(2, N + 1)]
    listComprehenSieve(A, N)
    print time.time() - tStart

def era1():
    N = input('Escriu el terme n: ')
    realEra(N)

# Es triguen 14.89 segons a completar aquesta funcio
# en un Mac Mini amb un Intel P8600. 
# Python 2.6.2 - Snow Leopard 10.6.8
def era2():
    realEra(10000000)

def factorp():
    n = input('Introdueix el nombre a factoritzar: ')
    if n == 1:
        return [1]
    A = [i for i in range(2, n + 1)]
    tStart = time.time()
    listComprehenSieve(A, n)
    iPrime = 0
    factorList = []
    while n != 1:
        if A[iPrime] != -1 and n % A[iPrime] == 0:
            factorList.append(A[iPrime])
            n = n / A[iPrime]
        else:
            iPrime = iPrime + 1
    print time.time() - tStart
    print factorList

def fermatp():
    n = input('Escriu un valor n: ')
    aValues = [2, 3, 5]
    for a in aValues:
        if (a ** (n - 1)) % n == 1:
            print 'Per n =', n, ' i a =', a, ' es podria considerar un nombre prim.'
        else:
            print 'Per n =', n, ' i a =', a, ' es podria considerar un nombre compost.'

cProfile.run('era5()')

