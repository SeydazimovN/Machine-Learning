import sys, networkx as nx, matplotlib.pyplot as plt

cntV = 0
vertex = dict()
value = {}
name = []
edges = []

def add_new_edge(v, to) :
	edges.append( (v, to) )
	print >>f1, v, to	
	print >>f1, name[v], name[to]

name.append("AnimalPlanet");
cur = -1;
file = open('data.txt', 'r')
f1 = open('graph.txt', 'w')
for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	# print all
	par = 0
	print all
	for i in range(len(all)) :
		# print all[i], 
		if (vertex.has_key(all[i]) == False) :
			cntV += 1;
			value[all[i]] = cntV;
			cur = cntV;
			vertex[all[i]] = True;
			name.append(all[i])
		else :
			cur = value[all[i]];
			
		# print (cur)
		add_new_edge(par, cur);
		par = cur

nodes = range(cntV + 1)
node_sizes = []
labels = {}

for i in nodes:
	node_sizes.append(2100)
	if (i == 0) : node_sizes[0] = 5000;
	labels[i] = name[i];

g = nx.DiGraph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)

# print g
print name

# nx.draw_networkx(g, node_size = node_sizes, labels=labels, with_labels=True)    
# plt.show()





