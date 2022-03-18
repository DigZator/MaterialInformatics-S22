import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.manifold import MDS

with open("E:\\Seagate Drive\\OM\\4th Semester Material\\Material Informatics\\Tutorial 2\\Data\\Two_pc_corr.csv") as file_name:
	array = np.loadtxt(file_name, delimiter=",")
	print(array.shape)
	arr = array[:, 0:65025]
	print(arr.shape)

embedding = MDS(n_components = 3)
val = embedding.fit_transform(arr)
#print(val)
#print(val.shape)
print("Stress for 65025 Features - ", embedding.stress_)

xaxis = val[:, :1]
yaxis = val[:, 1:2]
zaxis = val[:, 2:]
c = []
for i in range(300):
	c.append(i//50)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(xaxis, yaxis, zaxis, c=c)
#fig.colorbar()
plt.show()

embedding = MDS(n_components = 3)
val = embedding.fit_transform(array)
#print(val)
#print(val.shape)
print("Stress for 130050 Features - ", embedding.stress_)

xaxis = val[:, :1]
yaxis = val[:, 1:2]
zaxis = val[:, 2:]
c = []
for i in range(300):
	c.append(i//50)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(xaxis, yaxis, zaxis, c=c)
#fig.colorbar()
plt.show()