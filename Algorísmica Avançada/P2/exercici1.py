#
# exercici1.py
#
# description: Stoopid program to draw first exercise's graph
#
# author: olopezsa13
#

import matplotlib.pyplot as plt
import networkx as nx

def main():
    g = nx.Graph()
    for i in range(5):
        g.add_node(i + 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 5)
    nx.draw(g)
    plt.show()

main()
