read = lambda : map(str, raw_input().split())
yes = 0
no = 0
good = 0
for I in range(169):	
	cl, a1, a2, a3, a4, a5, a6, something = read();
	cl = int(cl)
	a1 = int(a1)
	a2 = int(a2)
	a3 = int(a3)
	a4 = int(a4)
	a5 = int(a5)
	a6 = int(a6)
	cnt = 0
	if (a1 == 1) : cnt += 1
	if (a2 == 1) : cnt += 1
	if (a3 == 1) : cnt += 1
	if (a4 == 1) : cnt += 1
	if (a5 == 1) : cnt += 1
	if (a6 == 1) : cnt += 1	
	if (cnt == 2) :
		if (cl == 1) :
			good += 1
		yes += 1
	else :
		if (cl == 0) :
			good += 1
		no += 1
	
print good	
print yes
print no
	