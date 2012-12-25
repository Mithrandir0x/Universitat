# B_ORIOL_LOPEZSANCHEZ.py

import networkx as nx

# El graf a ser analitzat.
G = None

# Els nodes del graf G que no tenen cap aresta que apunti cap a ells.
no_incoming_nodes = []

def llegir_graph():
    """
    Llegeix el graf.
    """
    global G
    name = raw_input("Doneu el nom del graf: ")
    G = nx.read_adjlist(name, create_using = nx.DiGraph(), nodetype = int)

"""
def dev_readGraph():
    global G
    G = nx.read_adjlist("dev_graph_1", create_using = nx.DiGraph(), nodetype = int)
"""

def search_undirected_nodes():
    """
    Guarda a "no_incoming_nodes" els nodes del graf que no tenen cap aresta que apunti
    cap a ells.

    Aquest metode te complexitat O(|v|+|e|). On |v| es el nombre de vertex i |e| el
    nombre d'arestas del graf G.
    """
    global no_incoming_nodes
    node_edges = {}
    for node in G:
        if not node in node_edges:
            node_edges[node] = 0
        neighborhood = G.neighbors(node)
        for neighbor in neighborhood:
            if neighbor in node_edges:
                node_edges[neighbor] += 1
            else:
                node_edges[neighbor] = 1
    for node, neighbors in node_edges.iteritems():
        if neighbors == 0:
            no_incoming_nodes.append(node)

def topological_sorting():
    """
    Retorna un vector amb els nodes del graf G ordenats topologicament.

    Te complexitat O(|v|+|e|). On |v| es el nombre de vertex i |e| el
    nombre d'arestas del graf G.
    """
    topologicalSortedList = []

    def visit_node(n):
        """
        Desde el node "n", visita cadascun dels seus veins, i els marca com
        a visitats.
        """
        G.add_node(n, visited = True)
        for neighbor in G[n]:
            if not 'visited' in G.node[neighbor]:
                visit_node(neighbor)
        topologicalSortedList.insert(0, n)

    for n in no_incoming_nodes:
        visit_node(n)

    return topologicalSortedList

def main():
    llegir_graph()
    for node in G:
        print node
    # search_undirected_nodes()
    # print topological_sorting()

if __name__ == "__main__":
    main()
