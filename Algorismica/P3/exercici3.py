#
# exercici3.py
#
# autor: olopezsa13
#

def acro():
    frase = input('Escriu una frase per acronimitzar-la: ')
    acronim = ''
    for paraula in frase.split(' '):
        if len(paraula) > 0:
            acronim = acronim + paraula[0].upper()
    print acronim

def paraules():
    frase = input('Escriu una frase: ')
    print len(frase.split(' '))

def cesar():
    abecedari = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    clau = input('Escriu la clau del xifratge: ')
    frase = input('Escriu la frase a xifrar: ')
    xifrat = ''
    for i in range(0, len(frase)):
        n = abecedari.find(frase[i].upper())
        xifrat = xifrat + abecedari[n + clau]
    print xifrat

def lyrics():
    fitxer = open('lletra.txt', 'r')
    text = fitxer.readlines()
    fitxer.close()
    for linea in text:
        print linea,
    print

def sequencia():
    fitxer = open('lletra.txt', 'r')
    text = fitxer.readlines()
    fitxer.close()
    possibleT = False
    vegades = 0
    for linea in text:
        for i in range(0, len(linea)):
            if linea[i] == 't':
                possibleT = True
            elif possibleT and linea[i] == 'h':
                possibleT = False
                vegades = vegades + 1
            else
                possibleT = False
    print vegades

def paraula():
    fitxer = open('lletra.txt', 'r')
    text = fitxer.readlines()
    fitxer.close()
    parCercar = input('Escriu la paraula a ser cercada: ')
    vegades = 0
    for linea in text:
        vegades = vegades + linea.count(parCercar)
    print parCercar

