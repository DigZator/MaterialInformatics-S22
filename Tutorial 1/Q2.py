import numpy as np
import matplotlib
from matplotlib import pyplot as plt

#2. Write a code to generate 2 microstructures using nucleation and growth. 
#   Create Equiaxed and elongated morphology. 
#   Calculate fraction of grain boundary and grain interior.
#   [50 grains, 100 x 100 grid size]

side = 100
board = np.zeros((side,side))

no_nuc = 50
nuc = [i for i in range(1,no_nuc+1)]

row = np.array([i for i in range(side)])
#print(row)
sel_row = np.random.choice(row, no_nuc)
#print(sel_row)
sel_col = np.random.choice(row, no_nuc)
#print(sel_col)
coord = [ [ sel_row[i], sel_col[i]] for i in range(len(sel_col))]
#print(nuc_coord)

for i in range(50):
	#print("Nucleus Coord - ", nuc_coord[i], "Nucleus Colour - ", nuc[i])
	board[coord[i][0]][coord[i][1]] = nuc[i]

# coord = [[20,50]]
# board[coord[0][0]][coord[0][1]] = nuc[0]

vx = 0.8
vy = 0.4

t = 1
nt = 10
meth = 1
#init -> 
if meth == 0: #Method 1 - 
	while (t < nt):
		#x = vx*t
		#y = vy*t
		i = 0
		j = 0
		for k in range(0,no_nuc):
			while ((i < vx*t) and (coord[k][0] + i < side)):
				while (((i/(vx*t))**2 + (j/(vy*t))**2 < 1)):
					if ( (coord[k][1] + j < side) and (coord[k][0] + i < side) and (board[coord[k][0] + i][coord[k][1] + j] == 0)):
						board[coord[k][0] + i][coord[k][1] + j] = nuc[k]            
					if ((coord[k][1] + j < side) and (coord[k][0] - i >= 0) and (board[coord[k][0] - i][coord[k][1] + j] == 0)):
						board[coord[k][0] - i][coord[k][1] + j] = nuc[k]
 	   	        
					if ((coord[k][1] - j >= 0) and (coord[k][0] + i < side) and (board[coord[k][0] + i][coord[k][1] - j] == 0)):
						board[coord[k][0] + i][coord[k][1] - j] = nuc[k]
 	   	        
					if ((coord[k][1] - j >= 0) and (coord[k][0] - i >= 0) and (board[coord[k][0] - i][coord[k][1] - j] == 0)):
						board[coord[k][0] - i][coord[k][1] - j] = nuc[k]
					
					j = j + 1
				j = 0
				i = i + 1
			i = 0
			t = t + 1
			#plt.imshow(board)
			#plt.show()
elif meth == 1: #Method 2
	gra_board = np.zeros((side,side), dtype = np.int8)
	for i in range(side):
		for j in range(side):
			if board[i][j] == 0:
				dist = []
				for gra in range(no_nuc):
					dist.append((i-coord[gra][0])**2 + (j-coord[gra][1])**2)
				gra_board[i][j] = np.argmin(dist)
	print(gra_board)
	while (t<nt):
		for i in range(side):
			for j in range(side):
				if board[i][j] == 0:
					grain = gra_board[i][j]
					if ( ((i - coord[grain][0])/(vx*t))**2 + ((j - coord[grain][1])/(vy*t))**2 < 1):
						board[i][j] = nuc[grain]
						#print("hi", board[i][j], grain)
		t = t + 1
		plt.imshow(board, cmap = "YlGnBu")
		#plt.colorbar()
		plt.show()
elif meth == 2: #Method 3
	while (t<nt):
		for i in range(side):
			for j in range(side):
				if board[i][j] == 0:
					for grain in range(no_nuc):
						if ( ((i - coord[grain][0])/(vx*t))**2 + ((j - coord[grain][1])/(vy*t))**2 < 1):
							board[i][j] = nuc[grain]
							#print("Hi")
						#print("hi", board[i][j], grain)
		print(t)
		t = t + 1
		#plt.imshow(board, cmap = "YlGnBu")
		#plt.colorbar()
		#plt.show()
elif meth == 3:
	check_p = np.zeros((side,side))
	while (t<nt):
		check = np.zeros((side,side))
		hold = np.zeros((side,side))
		for i in range(side):
			for j in range(side):
				if board[i][j] == 0:
					for grain in range(no_nuc):
						if ( ((i - coord[grain][0])/(vx*t))**2 + ((j - coord[grain][1])/(vy*t))**2 < 1):
							check[i][j] += 1
							if check[i][j] == 1:
								hold[i][j] = nuc[grain]
		for i in range(side):
			for j in range(side):
				if ((board[i][j] == 0) and (check[i][j] == 1)):
					board[i][j] = hold[i][j]
				if ((board[i][j] == 0) and check[i][j] > 1):
					board[i][j] = 60

		t = t+1
		plt.imshow(board, cmap = "YlGnBu")
		plt.show()
		print(t)

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]



plt.imshow(board, cmap = "YlGnBu")
plt.colorbar()
plt.show()