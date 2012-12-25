
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("spam")
G.add_edge(1, 2)
print(G.nodes())
print(G.edges())

G = nx.petersen_graph()
nx.draw(G)
plt.show()
