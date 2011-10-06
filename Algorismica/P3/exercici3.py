#
# exercici3.py
#
# autor: olopezsa13
#
# -*- coding: latin-1 -*-
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
    filtre = ' |,.?!'
    clau = input('Escriu la clau del xifratge: ')
    frase = input('Escriu la frase a xifrar: ')
    xifrat = ''
    for i in range(0, len(frase)):
        if not frase[i] in filtre:
            n = abecedari.find(frase[i].upper())
            nouCar = n + clau
            if n + clau >= len(abecedari):
                nouCar = nouCar - len(abecedari)
            xifrat = xifrat + abecedari[nouCar]
        else:
            xifrat = xifrat + frase[i]
    print xifrat

def getLyricsLines(filename):
    try:
        fitxer = open(filename, 'r')
        text = fitxer.readlines()
        fitxer.close()
        return text
    except IOError:
        print "El fitxer no esta disponible."
        return []

def lyrics():
    text = getLyricsLines('lletra.txt')
    for linea in text:
        print linea,
    print

def realSearch(needle):
    text = getLyricsLines('lletra.txt')
    vegades = False
    for linea in text:
        vegades = vegades + linea.count(needle)
    return vegades

def sequencia():
    print realSearch('th')

def paraula():
    parCercar = input('Escriu la paraula a ser cercada: ')
    print realSearch(parCercar)

cesar()

