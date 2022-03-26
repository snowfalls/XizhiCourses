from matplotlib import pyplot  as plt
import networkx as nx
G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_nodes_from([3])
nx.add_cycle(G, [1,2,3])
G.add_edge(1,2)
G.add_edges_from([(2,3)])
nx.draw(G)
plt.savefig("E:/youxiangtu.png")
plt.show()