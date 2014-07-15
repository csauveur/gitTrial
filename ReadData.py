import os
import csv
import numpy as np
import matplotlib.pylab as plt

# y helper; double = means quality check, where one = is an assignment
def ourfit(x,y,deg,xi = None):
    if xi == None:
        xi = x
    fitCoeff = np.polyfit(x, y, deg)
    fitPoly = np.poly1d(fitCoeff)
    return fitPoly(xi)

dirName = '/Users/sauveur_c/git/Random Data'
fileName = 'sampleData.dat'

# reading the data from our files
with open(os.path.join(dirName,fileName), 'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
data.pop(0)

# casting them from str to int/float
x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]

deg = 2

yFitValues = ourfit(x,y,deg)
xRandom = [4.5,6.5,8.5]
yFitRandom = ourfit(x,y,deg,xRandom)
zFitValues = ourfit(x,z,deg)


# yFitCoeff = np.polyfit(x, y, deg)
# yFitPoly = np.poly1d(yFitCoeff)
# yFitValues =  yFitPoly(x)
# 
# zFitCoeff = np.polyfit(x, z, deg)
# zFitPoly = np.poly1d(zFitCoeff)
# zFitValues =  zFitPoly(x)
# 
# print yFitCoeff
# print yFitPoly
# print yFitValues


plt.figure()
plt.plot(x,y, 'o')
plt.plot(x,yFitValues)
plt.plot(xRandom,yFitRandom, 'x')
plt.plot(x,z, 'o')
plt.plot(x,zFitValues)
plt.xlim(0,10)
plt.show()
