p = [[[0 for k in range(10)] for j in range(10)] for i in range(10)]

def getSport(name) :
	if (name == 'fight') : return 0
	if (name == 'team_game') : return 1
	if (name == 'versus') : return 2
def getLesson(name) :
	if (name == 'logic') : return 0
	if (name == 'art') : return 1
	if (name == 'humanities') : return 2	
def getColor(name) :
	if (name == 'red') : return 0
	if (name == 'green') : return 1
	if (name == 'blue') : return 2		
def getAnimal(name) :
	if (name == 'mammal') : return 0
	if (name == 'bird') : return 1
	if (name == 'fish') : return 2
	if (name == 'reptile') : return 3				
def getFriend(name) :
	if (name == 'yes') : return 0
	if (name == 'no') : return 1	
	
file = open('data.txt', 'r')
num = [0] * 20
cnt = [0] * 5
for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	N = len(all)
	num[1] = getSport(all[1])
	num[2] = getLesson(all[2])
	num[3] = getColor(all[3])
	num[4] = getAnimal(all[4])
	num[5] = getFriend(all[5])
	p[num[5]][1][num[1]] += 1
	p[num[5]][2][num[2]] += 1
	p[num[5]][3][num[3]] += 1
	p[num[5]][4][num[4]] += 1	
	cnt[num[5]] += 1
	
pr = [[[0 for k in xrange(10)] for j in xrange(10)] for i in xrange(10)]

def getCNT(x) :
	if (x == 1) : return 3
	if (x == 2) : return 3
	if (x == 3) : return 3
	if (x == 4) : return 4	

for k in range(1, 5) :
	count = getCNT(k);
	for Q in range (count) :
		pr[0][k][Q] = 1.0 * p[0][k][Q] / cnt[0]
		pr[1][k][Q] = 1.0 * p[1][k][Q] / cnt[1]		
		
name, sport, lesson, color, animal = map(str, raw_input().split(' '))
print (name, sport, lesson, color, animal)

sport_num = getSport(sport)
lesson_num = getLesson(lesson)
color_num = getColor(color)
animal_num = getAnimal(animal)

p_yes = pr[0][1][sport_num] * pr[0][2][lesson_num] * pr[0][3][color_num] * pr[0][4][animal_num];
p_no = pr[1][1][sport_num] * pr[1][2][lesson_num] * pr[1][3][color_num] * pr[1][4][animal_num];

print (p_yes)
print (p_no)

if (p_yes >= p_no) : 
	ans = name + " is your friend"
else : 
	ans = name + " is not your friend"
print (ans)
