#
# exercici7.py
#
# autor: olopezsa13
#

import math

def realExponential(A, N):
    if N == 1:
        return A
    else:
        return realExponential(A, math.floor(N / 2.0)) * realExponential(A, math.ceil(N / 2.0))

def exponent(A, N):
    if N <= 0:
        print '1'
    else:
        print realExponential(A, N)

def realReverse(frase):
    if len(frase) <= 1:
        return frase
    else:
        mitg = len(frase) / 2
        esquerra = realReverse(frase[:mitg])
        dreta = realReverse(frase[mitg:])
        return dreta + esquerra

def reverse(frase):
    f = realReverse(frase)
    print f

reverse('Hola, com estas?')

