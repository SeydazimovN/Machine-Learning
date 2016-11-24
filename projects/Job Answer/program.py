p = [[[0 for k in xrange(10)] for j in xrange(10)] for i in xrange(10)]

def getAcademy(name) :
	if (name == 'bachelor') : return 0
	if (name == 'magister') : return 1
	if (name == 'doctor') : return 2
def getExperience(name) :
	if (name == 'yes') : return 0
	if (name == 'no') : return 1
def getEnglish(name) :
	if (name == 'elementary') : return 0
	if (name == 'intermediate') : return 1
	if (name == 'advanced') : return 2		
def getKnowledge(name) :
	if (name == 'low') : return 0
	if (name == 'medium') : return 1
	if (name == 'high') : return 2
def getAnswer(name) :
	if (name == 'accepted') : return 0
	if (name == 'rejected') : return 1	
	
file = open('data.txt', 'r')
num = [0] * 20
cnt = [0] * 5
for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	N = len(all)
	num[1] = getAcademy(all[1])
	num[2] = getExperience(all[2])
	num[3] = getEnglish(all[3])
	num[4] = getKnowledge(all[4])
	num[5] = getAnswer(all[5])
	p[num[5]][1][num[1]] += 1
	p[num[5]][2][num[2]] += 1
	p[num[5]][3][num[3]] += 1
	p[num[5]][4][num[4]] += 1	
	cnt[num[5]] += 1
	
pr = [[[0 for k in xrange(10)] for j in xrange(10)] for i in xrange(10)]

def getCNT(x) :
	if (x == 1) : return 3
	if (x == 2) : return 2
	if (x == 3) : return 3
	if (x == 4) : return 3	

for k in range(1, 5) :
	count = getCNT(k);
	for Q in range (count) :
		# yes
		pr[0][k][Q] = 1.0 * p[0][k][Q] / cnt[0]
		# no
		pr[1][k][Q] = 1.0 * p[1][k][Q] / cnt[1]		
		
name, academy, experience, english, knowledge = map(str, raw_input().split(' '))
print (name, academy, experience, english, knowledge)

academy_num = getAcademy(academy)
experience_num = getExperience(experience)
english_num = getEnglish(english)
knowledge_num = getKnowledge(knowledge)

p_yes = pr[0][1][academy_num] * pr[0][2][experience_num] * pr[0][3][english_num] * pr[0][4][knowledge_num]
p_no = pr[1][1][academy_num] * pr[1][2][experience_num] * pr[1][3][english_num] * pr[1][4][knowledge_num]

print (p_yes)
print (p_no)

if (p_yes >= p_no) : 
	ans = name + " accepted to our job:)"
else : 
	ans = name + " got rejected :("
print (ans)
