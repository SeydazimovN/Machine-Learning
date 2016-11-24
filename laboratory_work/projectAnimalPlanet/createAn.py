
file = open('animals.txt', 'r')
cnt = 0
graph = []
for line in file:
	cnt += 1
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	if (cnt % 2) : 
		all = map(int, all);
		v = all[0];
		to = all[1];
		print v, to
		graph.append([v,to]);
	print all
	
	
