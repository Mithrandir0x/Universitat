#
# exercici8.py
#
# autor: olopezsa13
#

import genetic
import math
import time

def func1d(x):
    return x * ( math.sin(10 * math.pi * x) ) + 1.0

def frange1d(start, end, inc):
    y = float(start)
    end = float(end)
    inc = float(inc)
    while y < end:
        yield y
        y += inc

# Resultats donats pels valors demanats
# inc       x              f(x)           temps              '# crides a f'
# 0.01      1.85           2.85           0.000525951385498  301
# 0.0001    1.8505         2.85027170841  0.0501379966736    30,001
# 0.000001  1.85054699995  2.85027376657  5.33162999153      3,000,001
def search1d(res):
    yMax = float('-inf')
    xMax = yMax
    y = yMax
    nProc = 0
    tStart = time.time()
    for x in frange1d(-1, 2, res):
        nProc += 1
        y = func1d(x)
        if y > yMax:
            yMax = y
            xMax = x
    tEnd = time.time()
    print xMax, yMax, tEnd - tStart, nProc

# Clase per representar un vector de 2 reals
class Vector2():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def func2d(v):
    return 200.0 - ( ( v.x ** 2.0 + v.y - 11.0 ) ** 2.0 ) - ( ( v.x + v.y ** 2.0 - 7.0 ) ** 2.0 )

#
def frange2d(vStart, vEnd, inc):
    v = Vector2(vStart.x, vStart.y)
    while v.x <= vEnd.x:
        while v.y <= vEnd.y:
            yield v
            v.y += inc
        v.x += inc
        v.y = vStart.y

# Busca el maxim de la funcio dins l'interval definit pels vectors
# vStart, que ha de ser l'extrem inferior esquerra i vEnd, que ha
# de ser l'extrem superior de la dreta.
def segmentedSearch2d(vStart, vEnd, res):
    zMax = float('-inf')
    pMax = Vector2(float('-inf'), float('-inf'))
    for p in frange2d(vStart, vEnd, res):
        z = func2d(p)
        if z > zMax:
            zMax = z
            pMax.y = p.y
            pMax.x = p.x
    print 'Punt maxim a', pMax, 'amb valor', zMax

# Plot3D[200 - (x^2+y-11)^2-(x+y^2-7)^2, {x, -6, 6}, {y, -6, 6}, PlotRange -> {0, 300}]
def search2d(res=0.001):
    tStart = time.time()
    segmentedSearch2d(Vector2(-6, 0), Vector2(0, 6), res)
    segmentedSearch2d(Vector2(0, 0), Vector2(6, 6), res)
    segmentedSearch2d(Vector2(-6,-6), Vector2(0, 0), res)
    segmentedSearch2d(Vector2(0, -6), Vector2(6, 0), res)
    tEnd = time.time()
    print "S'ha trigat", tEnd - tStart, 's'

#genetic.genetic2(genetic.cost2)

