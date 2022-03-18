import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import cv2 as cv

RMS1 = np.random.rand(100,100)

same = True

if not same:
	RMS2 = np.random.rand(100,100)
else:
	RMS2 = np.copy(RMS1)

figure, axis = plt.subplots(3,2)

Gauss1 = cv.GaussianBlur(RMS1, (5,5), sigmaX = 1, sigmaY = 1)
Gauss2 = cv.GaussianBlur(RMS2, (5,5), sigmaX = 0.1, sigmaY = 8)

ret1, thresh1 = cv.threshold(Gauss1, 0.5, 1, cv.THRESH_BINARY)
ret2, thresh2 = cv.threshold(Gauss2, 0.5, 1, cv.THRESH_BINARY)

# create figure
fig = plt.figure(figsize=(8, 8))

# setting values to rows and column variables
rows = 3
columns = 2

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

plt.imshow(RMS1, cmap = 'gray')
plt.axis('off')
plt.title("Random Grid 1")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(RMS2, cmap = 'gray')
plt.axis('off')
plt.title("Random Grid 2")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(Gauss1, cmap = 'gray')
plt.axis('off')
plt.title("Gaussian Blur")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Gauss2, cmap = 'gray')
plt.axis('off')
plt.title("Gaussian Blur")

fig.add_subplot(rows, columns, 5)

# showing image
plt.imshow(thresh1, cmap = 'gray')
plt.axis('off')
plt.title("Threshold")
fig.add_subplot(rows, columns, 6)

# showing image
plt.imshow(thresh2, cmap = 'gray')
plt.axis('off')
plt.title("Threshold")

plt.show()