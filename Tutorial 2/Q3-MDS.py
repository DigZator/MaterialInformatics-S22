import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.manifold import MDS

with open("Data\\Two_pc_corr.csv") as file_name:
	array = np.loadtxt(file_name, delimiter=",")
	print(array.shape)
	arr = array[:, 0:65025]
	print(arr.shape)

embedding = MDS(n_components = 3, random_state = 1)
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

embedding = MDS(n_components = 3, random_state = 1)
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

show_scree = True

if show_scree:
	stress65 = []
	stress130 = []
	for i in range(1,11):
		embedding = MDS(n_components = i, random_state = 1)
		val = embedding.fit_transform(arr)
		stress65.append(embedding.stress_)
		embedding = MDS(n_components = i, random_state = 1)
		val = embedding.fit_transform(array)
		stress130.append(embedding.stress_)
	plt.plot(np.arange(1,11), stress65)
	plt.show()
	plt.plot(np.arange(1,11), stress130)
	plt.show()