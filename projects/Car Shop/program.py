import math
from operator import itemgetter, attrgetter

p = [[[0 for k in xrange(10)] for j in xrange(10)] for i in xrange(10)]

D = []

def getSize(name) :
	if (name == 'small') : return 0
	if (name == 'medium') : return 1
	if (name == 'big') : return 2
def getCountry(name) :
	if (name == 'germany') : return 0
	if (name == 'japan') : return 1
	if (name == 'russia') : return 2	
def getVolume(name) :
	if (name == '2.7') : return 0
	if (name == '3.5') : return 1
	if (name == '4.7') : return 2		
def getMark(name) :
	if (name == 'mercedes') : return 0
	if (name == 'toyota') : return 1
	if (name == 'mitsubishi') : return 2
def getQuality(name) :
	if (name == 'good') : return 0
	if (name == 'bad') : return 1	
	
file = open('data.txt', 'r')
num = [0] * 20
cnt = [0] * 5

name, size, country, volume, mark, cost_e, qual_e = map(str, raw_input().split(' '))
cost_e = float(cost_e)
qual_e = float(qual_e)

print (name, size, country, volume, mark, cost_e, qual_e)

for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	N = len(all)
	num[1] = getSize(all[1])
	num[2] = getCountry(all[2])
	num[3] = getVolume(all[3])
	num[4] = getMark(all[4])
	num[5] = getQuality(all[7])
	Cost = all[5]
	Qual = all[6]
	p[num[5]][1][num[1]] += 1
	p[num[5]][2][num[2]] += 1
	p[num[5]][3][num[3]] += 1
	p[num[5]][4][num[4]] += 1	
	cnt[num[5]] += 1
	
	Cost = float(Cost)
	Qual = float(Qual)
	
	euclid = (cost_e - Cost) * (cost_e - Cost) + (qual_e - Qual) * (qual_e - Qual)	
	euclid = math.sqrt(euclid)
	D.append((euclid, all[7]));	

D = sorted(D, key=itemgetter(0))

v1 = 0
v2 = 0
for i in range(11):
	if (D[i][1] == 'good') : v1 += 1;	
	if (D[i][1] == 'bad') : v2 += 1; 	

pr = [[[0 for k in xrange(10)] for j in xrange(10)] for i in xrange(10)]

def getCNT(x) :
	if (x == 1) : return 3
	if (x == 2) : return 3
	if (x == 3) : return 3
	if (x == 4) : return 3	

for k in range(1, 5) :
	count = getCNT(k);
	for Q in range (count) :
		pr[0][k][Q] = 1.0 * p[0][k][Q] / cnt[0]
		pr[1][k][Q] = 1.0 * p[1][k][Q] / cnt[1]		
		
size_num = getSize(size)
country_num = getCountry(country)
volume_num = getVolume(volume)
mark_num = getMark(mark)

p_yes = pr[0][1][size_num] * pr[0][2][country_num] * pr[0][3][volume_num] * pr[0][4][mark_num];
p_no = pr[1][1][size_num] * pr[1][2][country_num] * pr[1][3][volume_num] * pr[1][4][mark_num];

print ("Bayes: ")
print (p_yes)
print (p_no)
print ("KNN: ")
print (v1, v2)

if (p_yes >= p_no) :
	if (v1 > v2) :
		ans = name + " is good car to buy"
		print ans
		print "Both algorithms gave the same answer!"
	else :
		print "Error!"	
else :
	if (v2 > v1) :
		ans = name + " is bad car to buy"
		print ans
		print "Both algorithms gave the same answer!"								
	else :
		print "Error!"	
