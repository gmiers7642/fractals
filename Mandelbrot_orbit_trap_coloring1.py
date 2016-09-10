# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:08:18 2016

@author: glenn
"""

import numpy as np

# Bounds, initial defaults
Xmin = -2.5
Xmax = 1.5
Ymin = -2
Ymax = 2
maxIter = 200
gridSpc = 0.01
maxRad = 3.0
xTrap = 0.0
yTrap = 0.0
radius = 0.35

# Calculate the separate coordinates of the pixels to output
xCoords = np.arange(Xmin, Xmax, gridSpc)
yCoords = np.arange(Ymin, Ymax, gridSpc)

# Create an array to output the data to
arr = np.zeros(( len(xCoords), len(yCoords) ))

# Trap parameters
tCenter = complex(xTrap, yTrap)
tRadius = radius

#For all grid points
for y in yCoords:
    yindex = int((Ymax - y) / gridSpc )
    for x in xCoords:
        xindex = int((Xmax - x) / gridSpc )
        z = complex(x,y)
        c = z
        iter = 1
        while True:
            if(abs(z-tCenter) < tRadius):
                arr[yindex-1][xindex-1] = abs(z-tCenter)
                break
            if abs(z) > maxRad or iter >= maxIter:
                break
            z = z**2 + c
            iter += 1
