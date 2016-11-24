import sys, networkx as nx, matplotlib.pyplot as plt

nodes = range(10)
node_sizes = []
labels = {}
name = ["ROOT", "NURBA", "ANIMAL"]
for n in nodes:
        node_sizes.append(2100)
        labels[n] = 100 * n
        if (n <= 2) :
			labels[n] = name[n];

edges = []
edges.append( (1, 2) )
edges.append( (0, 3) )

g = nx.Graph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)

nx.draw_networkx(g, node_size = node_sizes, labels=labels, with_labels=True)    
plt.show()
