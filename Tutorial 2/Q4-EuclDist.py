import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import euclidean_distances as ED

# with open("E:\\Seagate Drive\\OM\\4th Semester Material\\Material Informatics\\Tutorial 2\\Data\\Two_pc_corr.csv") as file_name:
with open("Data\\Two_pc_corr.csv") as file_name:
	array = np.loadtxt(file_name, delimiter=",")
	print(array.shape)
	arr = array[:, 0:65025]
	print(arr.shape)

figure, axis = plt.subplots(1,3)
fig = plt.figure()
rows = 1
columns = 3

#print(ED(arr))

fig.add_subplot(rows, columns, 1)

plt.imshow(ED(arr))
plt.axis('off')
plt.title("ED")

pca = PCA(n_components = 3)
val = pca.fit_transform(arr)

#print(ED(val))

fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(ED(val))
plt.axis('off')
plt.title("PCA ED")

embedding = MDS(n_components = 3)
val = embedding.fit_transform(arr)

#print(ED(val))

fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(ED(val))
plt.axis('off')
plt.title("MDS ED")

plt.show()