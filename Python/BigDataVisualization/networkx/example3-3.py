from matplotlib import pyplot  as plt
import networkx as nx
G = nx.Graph()
G.add_nodes_from([1,2,3])
G.add_edges_from([(1,2), (1,3)])
nx.draw_networkx(G)
plt.show()