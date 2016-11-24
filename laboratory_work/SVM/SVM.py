import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style
style.use("ggplot")
# Just makes graph look nicer

from sklearn.metrics import accuracy_score

y = []
x = []

file = open('data.txt', 'r')
for line in file:
	all = []
	line = line.rstrip('\n')
	all = line.split(',');
	y.append(int(all[len(all) - 1]))
	temp = []
	for i in range(1, 10) :
		if (all[i] == '?') :
			cur = 0
		else :
			cur = float(all[i])
		temp.append(cur);
	x.append(temp)

X = np.array(x)

clf = svm.SVC(kernel = 'linear', C = 1)
clf.fit(X[0:400, :], y[0:400])

pred = clf.predict(X[401:600, :])
answer = y[401:600]
print (accuracy_score(answer, pred))

#w = clf.coef_[0]
#print(w)

#wx = X[:, 0]
#wy = X[:, 1]
#for i in range(0, 6) :
#	print w[0] * wx[i] + w[1] * wy[i]

#a = -w[0] / w[1]
#print clf.intercept_[0]

#xx = np.linspace(0, 12, 1000)
#yy = a * xx - clf.intercept_[0] / w[1]

#h0 = plt.plot(xx, yy, 'k-', label = "non weighted div")

#plt.scatter(X[:, 0], X[:, 1], c = y)
#plt.legend()
#plt.show() 
