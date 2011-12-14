#
# exercici8.py
#
# autor: olopezsa13
#

import math
import time
import cProfile

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
            yMax = y # 217 234 211.
            xMax = x
    tEnd = time.time()
    print xMax, yMax, tEnd - tStart, nProc

def vector2(x, y):
    return { 'x': float(x), 'y': float(y) }

def copyVector(vFrom, vTo):
    vTo['x'] = vFrom['x']
    vTo['y'] = vFrom['y']

def toString(v):
    return '(' + str(v['x']) + ', ' + str(v['y']) + ')'

def func2d(v):
    return 200.0 - ( ( v['x'] ** 2.0 + v['y'] - 11.0 ) ** 2.0 ) - ( ( v['x'] + v['y'] ** 2.0 - 7.0 ) ** 2.0 )

def frange2d(vStart, vEnd, inc):
    v = vector2(vStart['x'], vStart['y'])
    while v['x'] <= vEnd['x']:
        while v['y'] <= vEnd['y']:
            yield v
            v['y'] += inc
        v['x'] += inc
        v['y'] = vStart['y']

def search2d(res):
    zMax = float('-inf')
    for p in frange2d(vector2(-1, -1), vector2(0, 0), res):

search2d(0.1)

