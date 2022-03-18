import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

with open("Data\\Two_pc_corr.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

print(array.shape)
arr = array[:, :65025]
print(arr.shape)

print()

pca = PCA(n_components = 3)
val = pca.fit_transform(arr)
print(pca.explained_variance_ratio_)
print(val)

ax = plt.axes()
ax.plot(["PC1", "PC2", "PC3"], np.cumsum(pca.explained_variance_ratio_))
plt.show()

xaxis = val[:, :1]
yaxis = val[:, 1:2]
zaxis = val[:, 2:]
c = []
#print(xaxis,yaxis,zaxis)

for i in range(300):
	c.append(i//50)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(xaxis, yaxis, zaxis, c=c)
plt.show()

pca = PCA(n_components = 3)
val = pca.fit_transform(array)
print(val)

ax = plt.axes()
ax.plot(["PC1", "PC2", "PC3"], np.cumsum(pca.explained_variance_ratio_))
plt.show()

xaxis = val[:, :1]
yaxis = val[:, 1:2]
zaxis = val[:, 2:]

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(xaxis, yaxis, zaxis, c=c)
#fig.colorbar()
plt.show()