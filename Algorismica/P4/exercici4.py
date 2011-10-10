#
# exercici4.py
#
# autor: olopezsa13
#

import math

def mentre():
    n = input('Introdueix un valor numeric: ')
    i = 0
    suma = 0
    while i < n:
        suma = suma + i
    print suma

def mentre2():
    n = input('Introdueix un valor numeric: ')
    i = 0
    suma = 0
    while i < n:
        i = 2 * i + 1
        suma = suma + i
    print suma

def mentre3():
    suma = 0
    n = input()
    while n != 999:
        suma = suma + n
        n = input()
    print suma

def mentre4():
    n = input('Introdueix un valor numeric: ')
    suma = 0
    while n % 2 == 0:
        n = n / 2
        suma = suma + 1
    print suma

def inversio():
    print 'Inteligencia insuficient per fer aquest problema.'

def nota():
    qualificacions = {
        0 : 'Suspens',
        1 : 'Suspens',
        2 : 'Suspens',
        3 : 'Suspens',
        4 : 'Suspens',
        5 : 'Aprovat',
        6 : 'Aprovat',
        7 : 'Notable',
        8 : 'Notable',
        9 : 'Excelent',
        10 : 'Matricula'
    }

    try:
        nota = int(input('Escriu la nota a avaluar: '))
        if nota > 10:
            nota = 10
        elif nota < 0:
            nota = 0
        print qualificacions[nota]
    except ValueError:
        print 'El contingut introduit no es numeric.'

def dni():
    # Aixo es una col-leccio de caracters. Un vector es una coleccio
    # d'elements ordenats i associats per un valor numeric que
    # comenca per 0 i acaba fins a la longitud - 1 de la cadena entrada.
    lletres = 'TRWAGMYFPDXBNJZSQVHLCKE'
    try:
        rawDni = raw_input('Introdueix el DNI: ')
        if len(rawDni) != 8:
            print 'El DNI introduit es invalid.'
        else:
            dni = int(rawDni)
            print rawDni + lletres[dni % 23]
    except ValueError:
        print 'El contingut introduit no es numeric.'

def llista():
    print 'Consultar metode d"entrada amb el professor'

def otan():
    alfabetOtan = {
        'A' : 'Alpha',
        'B' : 'Bravo',
        'C' : 'Charlie',
        'D' : 'Delta',
        'E' : 'Echo',
        'F' : 'Foxtrot',
        'G' : 'Golf',
        'H' : 'Hotel',
        'I' : 'India',
        'J' : 'Juliet',
        'K' : 'Kilo',
        'L' : 'Lima',
        'M' : 'Mike',
        'N' : 'November',
        'O' : 'Oscar',
        'P' : 'Papa',
        'Q' : 'Quebec',
        'R' : 'Romeo',
        'S' : 'Sierra',
        'T' : 'Tango',
        'U' : 'Uniform',
        'V' : 'Victor',
        'W' : 'Whiskey',
        'X' : 'Xray',
        'Y' : 'Yankee',
        'Z' : 'Zulu'
    }

    par = input('Escriu una paraula: ')
    for i in range(len(par)):
        print alfabetOtan[par[i].upper()],
    print

otan()

