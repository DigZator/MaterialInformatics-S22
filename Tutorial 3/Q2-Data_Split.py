import csv
import numpy as np
from sklearn.model_selection import train_test_split as tts

use_pca = True

if use_pca:
	with open("Data\\PCA_Stress.csv") as file_name:
		data = np.loadtxt(file_name, delimiter=",")
		print(data.shape)
else:
	with open("Data\\MDS_Stress.csv") as file_name:
		data = np.loadtxt(file_name, delimiter=",")
		print(data.shape)

ran_split = False

if ran_split:
	X = data[:,0:3]
	Y = data[:,3]
	#print(X,Y)
	X_train, X_test, Y_train, Y_test = tts(X, Y, test_size = 0.166, shuffle = False)
	print(X.shape, Y.shape)
	print(X_test.shape, Y_test.shape)
	print(X_train.shape, Y_train.shape)
	# print(data)
	# print(X_test)
	# print(Y_test)
else:
	X_train = []
	X_test = []
	Y_train = []
	Y_test = []

	ratio = 0.3
	split = int((50 * ratio) // 1)

	for i in range(6):
		subdata = data[i*50:(i+1)*50]
		# print(subdata[0])
		X_test.append(subdata[0:split, 0:3])
		Y_test.append(subdata[0:split, 3])
		X_train.append(subdata[split:50, 0:3])
		Y_train.append(subdata[split:50, 3])
	X_test = np.array(X_test).reshape(split*6,3)
	Y_test = np.array(Y_test).reshape(split*6,1)
	X_train = np.array(X_train).reshape(300-(split*6),3)
	Y_train = np.array(Y_train).reshape(300-(split*6),1)

	print(X_test.shape, Y_test.shape)