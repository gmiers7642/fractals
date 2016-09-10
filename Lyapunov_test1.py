# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:08:18 2016

@author: glenn
"""

import numpy as np
from math import log10

# Bounds, initial defaults
Xmin = 0.0
Xmax = 4.0
Ymin = 0.0
Ymax = 4.0
pattern = 'AB'
gridSpc = 0.01
num_start_iter = 40
num_total_iter = 6000
z_init = 0.5

# Calculate the separate coordinates of the pixels to output
xCoords = np.arange(Xmin, Xmax, gridSpc)
yCoords = np.arange(Ymin, Ymax, gridSpc)

# Create an array to output the data to
arr = np.zeros(( len(xCoords), len(yCoords) ))

#For all grid points
for y in yCoords:
    yindex = int((Ymax - y) / gridSpc )
    for x in xCoords:
        xindex = int((Xmax - x) / gridSpc )
#        z = complex(x,y)
#        c = z
        iter = 1
        sum = 0
        while iter <= num_start_iter:
            z = z_init
            r = 0
            if(pattern[iter % len(pattern) == 'A'] ):
                r = x
            elif(pattern[iter % len(pattern) == 'B'] ):
                r = y
            x = r * x * (1 - x)
            sum += log10(abs(r*(1 - 2*x)))
            iter += 1
        arr[xindex-1][yindex-1] = sum / iter
    print yindex