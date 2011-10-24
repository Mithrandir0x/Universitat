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
    return mergedList.sort()

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

def eraIterative():
    N = input('Escriu el terme n: ')
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    for i in range(2, N + 1):
        A.append(i)
    tStart = time.time()
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
    
    print time.time() - tStart
    print A
    print B
    print mergeSort(A,B)

def era1():
    N = input('Escriu el terme n: ')
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    for i in range(2, N + 1):
        A.append(i)
    tStart = time.time()
    recursiveSieve(A, B, N)
    print time.time() - tStart
    print mergeSort(A,B)

def era2():
    N = 10000000
    A = [] # Tots els valors entre 2 i N
    B = [] # Llista on es guardaran tots els nombres primers
    for i in range(2, N + 1):
        A.append(i)
    tStart = time.time()
    recursiveSieve(A, B, N)
    primeList = mergeSort(A,B)
    print time.time() - tStart
    print len(primeList)

def factorp():
    # Highly damaged brain cells
    print

def fermatp():
    # brrrr
    print

fib1()

