import csv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

side = 256
board = np.zeros((6,side,side))
vol_frac = []

for i in range(6):
	file = open("Data\\{}.csv".format(i+1))
	csvreader = csv.reader(file)
	for row in csvreader:
		board[i][int(row[0])-1][int(row[1])-1] = int(row[2])

# for b in board:
# 	print(b)

for i in range(6):
	tot = board[i].sum()
	print("Volume Fraction of Microstructure - ", i+1, "is", 100*tot/(side**2))
	vol_frac.append(100*tot/(side**2))


file = open("Data\\Two_pc_corr.csv")

csvreader = csv.reader(file)
print()
col = []
for i in range(300):
	row = np.array([float(i) for  i in next(csvreader)[:65025]])
	vol = np.amax(row)
	print(i+1, " - ", vol*100, "\t\tDiff - ", abs(vol*100 - vol_frac[(299-i)//50]))
	col.append(vol*100)
	#print(i+1, "-", vol*100, vol_frac[(i)//50])
col = np.array(col).reshape((6,50))
print(np.sum(col, axis = 1)/50)
print(vol_frac)	