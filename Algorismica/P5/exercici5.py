#
# exercici5.py
#
# autor: olopezsa13
#

import math
import time

def realFib(f0, f1, i, n):
    if n == 0:
        return f0
    elif n == 1:
        return f1
    elif i == n:
        return f1 + f0
    else:
        return realFib(f1, f0 + f1, i + 1, n)

def fib1():
    n = input('Escriu per a quin terme "n" vols que calculi fibonacci: ')
    tStart = time.time()
    fibRes = realFib(0, 1, 2, n)
    tEnd = time.time()
    print 'Fibonacci(',n,') =', fibRes
    print 'Temps del calcul:', tEnd - tStart,'s'

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

def mergeSort(A, B):
    mergedList = B[:] # Copia del contingut de B, per evitar un alies
    mergedList.append('')
    mergedList[-1:] = A
    mergedList.sort() # El metode 'sort' no retorna res, modifica l'objecte
    return mergedList

def deleteNoneValuesFromList(A):
    [A.pop(i) for i in A
     if i == None]

# Solucio a forca bruta
def recursiveSieve(A, B, N):
    if A[0] > math.sqrt(N):
        return
    else:
        j = 0
        prime = A[0]
        B.append(prime)
        while j < len(A):
            if A[j] % prime == 0:
                A.pop(j)
            j = j + 1
        recursiveSieve(A, B, N)

# Solucio iterativa
def iterativeSieve(A, B, N):
    sqrtN = math.sqrt(N)
    prime = A[0]
    while prime < sqrtN:
        B.append(prime)
        j = 0
        while j < len(A):
            if A[j] % prime == 0:
                A.pop(j)
            j = j + 1
        prime = A[0]

def iterativeSieve2(A, B, N):
    sqrtN = math.sqrt(N)
    i = 0
    c2 = 0
    c1 = 0
    while A[i] < sqrtN:
        if A[i] != None:
            B.append(A[i])
            prime = A[i]
            j = i
            while j < len(A):
                if A[j] != None and A[j] % prime == 0:
                    A[j] = None
                j = j + 1
                c2 = c2 + 1
        i = i + 1
        c1 = c1 + 1
    print c1, c2

def era0():
    N = 100000
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    [A.append(i) for i in range(2, N + 1)]    
    tStart = time.time()
    iterativeSieve(A, B, N)
    print time.time() - tStart
    #print mergeSort(A,B)

def era3():
    N = 100000
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    [A.append(i) for i in range(2, N + 1)]    
    tStart = time.time()
    iterativeSieve2(A, B, N)
    print time.time() - tStart
    #print A
    #print B
    #print mergeSort(A,B)


def era1():
    N = input('Escriu el terme n: ')
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    for i in range(2, N + 1):
        A.append(i)
    tStart = time.time()
    recursiveSieve(A, B, N)
    print time.time() - tStart
    #print mergeSort(A,B)

# Anotacions
#    50000 ~0.26s (amb pop) | Intel C2D E8500 (VM Virtual Box) - Ubuntu 11.04 (Natty Narwhal)
#    50000 ~0.53s (amb pop) | Intel C2D E8500 - Windows 7 x64 | Python 2.6.2
#    50000 ~1.21s (amb pop) | Intel C2D P8600 (Mac Mini) - Snow Leopard 10.6.8 | Python 2.6.1
def era2():
    N = 50000
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    [A.append(i) for i in range(2, N + 1)]
    tStart = time.time()
    recursiveSieve(A, B, N)
    print time.time() - tStart

def factorp():
    # Llista dels nombres prims menors a 1000 calculats anteriorment amb la criba d'Eratostenes
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
        167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
        263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
        367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
        463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
        587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677,
        683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
        811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
        929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    iPrime = 0
    factorList = []
    n = input('Introdueix el nombre a factoritzar: ')
    tStart = time.time()
    while n != 1:
        try:
            if n % primeList[iPrime] == 0:
                factorList.append(primeList[iPrime])
                n = n / primeList[iPrime]
            else:
                iPrime = iPrime + 1
        except IndexError:
            print 'Nombre prim no trobat. Si us plau, calcular mes nombres prims per poder factoritzar correctament el nombre demanat.'
            break
    print time.time() - tStart
    print factorList

def fermatp():
    # brrrr
    print

