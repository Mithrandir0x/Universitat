# exercici2.py
#
# author: mithrandir0x

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
    for celsius in range(0, 100, 10):
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print "Celsius:", celsius, " | Fahrenheit:", fahrenheit

def exp():
    print "(a)", 4.0 / 10.0 + 3.5 * 2
    print "(b)", 10 % 4 + 6 / 2
    print "(c)", abs(4 - 20 / 3) ** 3
    print "(d)", sqrt(4.5 - 5.0) + 7 * 3
    print "(e)", 3 * 10 / 3 + 10 % 3
    print "(f)", 3L ** 3

def punts():
    print "Calcul de la pendent d'una recta donats 2 punts"
    x1, y1, x2, y2 = input("Donem els punts en format 'x1, y1, x2, y2': ")
    if x1 == x2:
        print "La pendent es indefinida."
    else:
        print "La pendent que dona la recta que passa per aquests 2 punts es:", ( y2 - y2 ) / ( x2 - x1 )

def euclid():
    print "Calcul de la distancia euclidiana entre dos punts"
    x1, y1, x2, y2 = input("Donem els punts en format 'x1, y1, x2, y2': ")
    inner = ( ( x2 - x1 ) ** 2 ) + ( ( y2 - y1 ) ** 2 )
    if inner < 0:
        print "No es pot calcular."
    else:
        print "La distancia es:", sqrt(inner)

def euclid2():
    print "El mateix que l'anterior"

def factmenor():
    print "Nivell d'inteligencia insuficient per fer aquest exercici."

def suma():
    print "Suma dels nombres menors de 100 que son multiples de 3 i 5"
    sum = 0
    for i in range(100):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print "El nombre es:", sum

 def divisible():
     print "Calcul del nombre natural mes petit que es divisible per 2, 3, 4, 5, 6, 7, 8, 9, i 10"