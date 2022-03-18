import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#import cv2 as cv

#1. Write a code to generate a random microstructure [50% black, 100 x 100 grid size]

side = 100

board = np.zeros((side,side))
bank = (side*side)/2

i = 0
j = 0


while (bank > 0):
	if (board[i][j] == 1):
		pass
	else:
		n = np.random.randint(2, size = (1)) 
		n = n[0]
		if n == 1:
			board[i][j] = 1
			bank = bank - 1
	i = i + 1
	if (i == side):
		i = 0
		j = j + 1
		if (j == side):
			j = 0
print(board)
print(board.sum())

plt.imshow(board, cmap = "gray")
plt.show()