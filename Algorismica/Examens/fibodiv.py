#
# fibodiv.py
#
# autor: olopezsa13
#

def fibodiv(n, k):
    nMultiples = 0
    f0 = 0
    f1 = 1
    while nMultiples < n:
        f = f0 + f1
        if f % k == 0:
            print 'Numero ', f, ' es multiplo de ', k
            nMultiples = nMultiples + 1
        f0 = f1
        f1 = f
