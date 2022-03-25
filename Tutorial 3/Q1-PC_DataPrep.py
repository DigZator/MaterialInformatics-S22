import csv
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import MDS

with open("Data\\Two_pc_corr.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",")
    print(array.shape)

use_pca = True

if use_pca:
    pca = PCA(n_components = 3)
    val = pca.fit_transform(array)
else:
    embedding = MDS(n_components = 3, random_state = 2)
    val = embedding.fit_transform(array)
#print(val)

with open("Data\\Stress.csv") as file_name:
    stress = np.loadtxt(file_name, delimiter=",")
    print(stress.shape)

stress = stress.reshape((300,1))
#print(stress)

print(val.shape, stress.shape)
data = np.hstack((val,stress))

print(data)
if use_pca:
    with open('Data\\PCA_Stress.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
else:
    with open('Data\\MDS_Stress.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
