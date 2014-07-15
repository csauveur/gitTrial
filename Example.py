import os
import csv
import numpy as np
import matplotlib.pylab as plt
import ExampleClass


dirName = '/Users/sauveur_c/git/Random Data'
fileName = 'sampleData.dat'

with open(os.path.join(dirName,fileName), 'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
data.pop(0)

x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]

# p = [y[i]*z[i] for i in range(len(data))]
# r = [y[i]-z[i] for i in range(len(data))]
# 
xyObj = ExampleClass.simpleOperations(x,y)
# print xyObj.productXY()

# print xyObj.differenceXY()
# 
# xzObj = ExampleClass.simpleOperations(x,z)
# yzObj = ExampleClass.simpleOperations(y,z)
# 
# print xzObj.differenceXY()
# print yzObj.differenceXY()
# 
# print xyObj.differenceXY()

# xyObj.printDefaults()
# xyObj.printDefaults(2,5,6)
# xyObj.printDefaults(1,2)
# xyObj.printDefaults(z=3)
# xyObj.printDefaults(z=3,x=7)

print xyObj.newFun()

