file = open('animals.txt', 'w')

name = []
edges = []

value = {}
vertex = dict()

def add_new_edge(v, to) :
	edges.append( (v, to) )
	print >>file, v, to	
	print >>file, name[v], name[to]

name.append("nothing");

def doit(current) :
	cur = -1
	if (vertex.has_key(current) == False) :
		cntV = len(name) + 1;
		value[current] = cntV;
		cur = cntV;
		vertex[current] = True;
		name.append(current)
	else :
		cur = value[current];
	return cur

while (True) :
	T = input();
	if (T == 0) :
		break;
	s1 = raw_input();
	s2 = raw_input();
	fromV = doit(s1)
	toV = doit(s2)	
	add_new_edge(fromV, toV);	
