# exercici2.py
#
# author: olopezsa13

import math

def futval():
    print "Aquest programa calcula el valor futur d'una determinada inversio a una quantitat d'anys desitjada."
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra l'interes anual: ")
    anys = input("Entra la quantitat d'anys: ")
    for i in range(anys):
        principal = principal * ( 1 + apr )
    print "La quantitat al cap de", anys, "es:", principal

def convert():
    print "Taula d'equivalencies Celsius a Fahrenheit"
    for celsius in range(0, 110, 10):
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print "Celsius:", celsius, " | Fahrenheit:", fahrenheit

def exp():
    print "(a)", 4.0 / 10.0 + 3.5 * 2
    print "(b)", float(10 % 4 + 6) / 2
    print "(c)", abs(4 - 20 / 3) ** 3
    #print "(d)", math.sqrt(4.5 - 5.0) + 7 * 3
    print "(d)", math.sqrt(5.0 -4.5) + 7 * 3
    print "(e)", 3 * 10 / 3 + 10 % 3
    print "(f)", 3L ** 3

def punts():
    print "Calcul de la pendent d'una recta donats 2 punts"
    x1, y1, x2, y2 = input("Donem els punts en format 'x1, y1, x2, y2': ")
    if x1 == x2:
        print "La pendent es indefinida."
    else:
        print "La pendent que dona la recta que passa per aquests 2 punts es:", ( y2 - y2 ) / ( x2 - x1 )

def euclid_real():
    print "Calcul de la distancia euclidiana entre dos punts"
    x1, y1, x2, y2 = input("Donem els punts en format 'x1, y1, x2, y2': ")
    inner = ( ( x2 - x1 ) ** 2 ) + ( ( y2 - y1 ) ** 2 )
    res = math.sqrt(inner)
    if inner < 0:
        print "No es pot calcular."
    return res

def euclid():
    res = euclid_real()
    print "La distancia euclidiana es:", res

def euclid2():
    res = euclid_real()
    print "La distancia euclidiana es:", int(res)

def factmenor():
    val = 6204484017332394393600000
    n = 1   # Valor del factorial
    cal = 1 # Resultat actual del calcul del factorial
    while cal < val:
        cal = cal * n
        n = n + 1
    print n

def suma():
    print "Suma dels nombres menors de 100 que son multiples de 3 i 5"
    sum = 0
    for i in range(100):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        print i, i % 3, i % 5, sum
    print "El nombre es:", sum

def divisible():
    print "Calcul del nombre natural mes petit que es divisible per 2, 3, 4, 5, 6, 7, 8, 9, i 10"
     print "Calcul del nombre natural mes petit que es divisible per 2, 3, 4, 5, 6, 7, 8, 9, i 10"print "Calcul del nombre natural mes petit que es divisible per 2, 3, 4, 5, 6, 7, 8, 9, i 10"