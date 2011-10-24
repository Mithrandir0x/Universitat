#
# exercici5.py
#
# autor: olopezsa13
#

import time

def realFib(f0, f1, i, n):
    if n == 0:
        return f0
    elif n == 1:
        return f1
    elif i == n:
        return f1 + f0
    if i < n:
        return realFib(f1, f0 + f1, i + 1, n)

def fib1():
    n = input('Escriu per a quin terme "n" vols que calculi fibonacci: ')
    tStart = time.clock()
    fibRes = realFib(0, 1, 2, n)
    tEnd = time.clock()
    print 'Fibonacci(',n,') =', fibRes
    print 'Temps del calcul:', tEnd - tStart, 'ms'

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

