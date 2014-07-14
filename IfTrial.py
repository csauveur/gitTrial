import os
import csv
import random as rand
import matplotlib.pylab as plt

x = range(1,10)
y = [(i+rand.random())**2 for i in x]
z =  [(i+rand.random()*2)**2 for i in x]
print x
print y 


plt.figure()
font = {'family': 'Computer Modern Roman', 'size':16}
plt.rc('font',**font)
plt.plot(x,y,'o', label= 'x values')
plt.plot(x,z,'o', label = 'y values')
plt.xlabel('x values')
plt.ylabel('y values')
plt.xlim(0,10)
plt.ylim(0,10)
plt.legend(loc='best')
plt.show()


DirName = 'Users/sauveur_c/Documents/workspace/randomdata'
FileName = 'sampleData.dot'

if not os.path.exists(dirName):
    os.makedirs(dirName)
    


datalist = list()
[datalist.append([x[i],y[i],z[i]]) for i in range(len(x))]

print datalist
with open(os.path.join(dirName,fileName), 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['x','y','z'])
    writer.writerows(datalist)

    
