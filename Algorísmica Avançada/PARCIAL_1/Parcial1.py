#
# Parcial1.py
#
# author: olopezsa13
#

import matplotlib.pyplot as plot
import networkx as nx

def euleriano(G):
    """
    Imprime por pantalla si el grafo es o no euleriano.

    Tiene complejidad O(|v|), donde |v| es el numero de vertices del grafo.
    """
    for nodo in G:
        vecinos = G.neighbors(nodo)
        if len(vecinos) % 2 != 0:
            print "El grafo no es euleriano."
            return
    print "El grafo es euleriano."

def puentes(G):
    """
    Imprime por pantalla las aristas puente del grafo.

    Tiene complejidad O(|v|), donde |v| es el numero de vertices del grafo.

    Implementación incorrecta. Consultar: http://en.wikipedia.org/wiki/Bridge_(graph_theory)#Bridge-Finding_Algorithm
    """
    hay_aristas_puente = False
    for nodo in G:
        aristas_entrantes = G.in_edges(nodo)
        if len(aristas_entrantes) == 1:
            print "La arista entre %s y %s es un puente." % aristas_entrantes[0]
            hay_aristas_puente = True
    if not hay_aristas_puente:
        print "El grafo no tiene ninguna arista puente."

def leer_grafo(ruta):
    return nx.read_adjlist(ruta, create_using = nx.DiGraph())

"""
Juegos de pruebas:

    "euler_1.in" - Grafo euleriano. Todos sus nodos tienen solamente 2 vecinos. Ademas,
        no tiene aristas puente.
    "euler_2.in" - Grafo en que dos de sus nodos tienen 3 vecinos. No es euleriano.
    "puentes_4.in" - Grafo con varias aristas puente.

Salida esperada:

euler_1.in
El grafo es euleriano.

euler_3.in
El grafo no es euleriano.

euler_1.in
El grafo no tiene ninguna arista puente.

puentes_4.in
La arista entre A y B es un puente.
La arista entre B y E es un puente.
La arista entre B y D es un puente.
La arista entre A y G es un puente.
La arista entre E y F es un puente.
La arista entre H y I es un puente.
La arista entre C y H es un puente.
"""

def execute_tests():
    tests = ["euler_1.in", "euler_3.in"]
    for test_grafo in tests:
        print test_grafo
        gr = leer_grafo(test_grafo)
        euleriano(gr)
        print

    tests = ["euler_1.in", "puentes_4.in"]
    for test_grafo in tests:
        print test_grafo
        gr = leer_grafo(test_grafo)
        puentes(gr)
        print

execute_tests()
