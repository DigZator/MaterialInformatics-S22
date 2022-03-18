from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
from matplotlib  import pyplot as plt

xd = yd = 100

seeds = 30  #number of grains
book = []                                                                                                          
for i in range(seeds):    
  x = np.random.randint(0, xd)
  y = np.random.randint(0, yd)
  book.append([x, y])

vor = Voronoi(book)
fig = voronoi_plot_2d(vor)
plt.show()