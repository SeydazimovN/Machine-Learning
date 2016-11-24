info = raw_input().split();	

file = open('data.txt', 'a')
for i in range(len(info)) :
	print >>file, info[i],
	
