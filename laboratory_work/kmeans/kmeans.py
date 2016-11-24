import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import randint

img = cv2.imread('home.jpg')
height, width, channels = img.shape

x = []
y = []
z = []
color = []
M = int(input())

cx = []
cy = []
cz = []
for i in range(0, M) :
	cx.append(randint(0, 255))
	cy.append(randint(0, 255))
	cz.append(randint(0, 255))				
def sqr(x) :
	return x * x;	

for i in range(0, height) :
	for j in range(0, width) :
		x.append(img[i][j][0])	
		y.append(img[i][j][1])
		z.append(img[i][j][2])
		color.append(0);

for rep in range(0, 200):	
	for i in range(0, N) :
		MIN = (3000000);
		picked = -1
		for z in range(0, M) :
			dist = sqr(x[i] - cx[z]) + sqr(y[i] - cy[z]) + sqr(z[i] - cz[i]);
			if (dist < MIN) :
				MIN = dist
				picked = z
		color[i] = picked	
		
	for z in range(0, M) :
		sumx = 0
		sumy = 0
		cnt = 0
		for i in range(0, N) :
			if (color[i] == z) :
				sumx += x[i]
				sumy += y[i]
				cnt += 1;
		if (cnt != 0) :
			sumx /= cnt
			sumy /= cnt
		cx[z] = sumx
		cy[z] = sumy

# for i in range(0, N) : color[i] += 1;

plt.scatter(x, y, c = color);
plt.scatter(cx, cy, marker = '*', color = 'red');
plt.show();		

# print cx
# print cy

