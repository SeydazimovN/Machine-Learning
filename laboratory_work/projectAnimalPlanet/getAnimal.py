import Image

# Apple = Image.open("apple.jpg")    
# Apple.show()
# instead of using .open and .show(), 
# save the image to show it with the webbrowser module

def openImg(AnimalName) :
	print (AnimalName)
	last = ".jpg";
	AnimalName = AnimalName + last;
	print AnimalName
	filename = AnimalName
	import webbrowser
	webbrowser.open(filename)

info = raw_input().split();
cnt = 0
answer = []
file = open('data.txt', 'r')
print info
for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(' ');
	bad = 0
	for i in range(len(info)) :
		if (all[i] != info[i]) :
			bad = 1;
	if (bad == 0) :
		answer.append(all[len(all) - 1]);
		cnt = 1
		
if (cnt > 0) :
	for i in range(len(answer)) :
		print (answer[i]);
		AnimalName = answer[i];
		openImg(AnimalName);
else :
	print ("This kind of animal does not exist in our planet.")
	print ("Try to search in another planet")
