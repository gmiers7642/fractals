# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:08:18 2016

@author: glenn
"""
import numpy as np

class Mandelbrot(object):
    def __init__(self, params={'Xmin':-2.5, 'Xmax':1.5, 'Ymin':-2.0, 'Ymax':2.0,
                     'maxIter':100, 'maxRad':3.0, 'gridSpc':0.05}):
        self.Xmin = params['Xmin']
        self.Xmax = params['Xmax']
        self.Ymin = params['Ymin']
        self.Ymax = params['Ymax']
        self.maxIter = params['maxIter']
        self.maxRad = params['maxRad']
        self.gridSpc = params['gridSpc']

    def setup(self):
        # Calculate the separate coordinates of the pixels to output
        self.xCoords = np.arange(self.Xmin, self.Xmax, self.gridSpc)
        self.yCoords = np.arange(self.Ymin, self.Ymax, self.gridSpc)
        # Create an array to output the data
        self._image = np.zeros(( len(self.xCoords), len(self.yCoords) ))

    def calc_image(self):
        #For all grid points
        for y in self.yCoords:
            yindex = int((self.Ymax - y) / self.gridSpc )
            for x in self.xCoords:
                xindex = int((self.Xmax - x) / self.gridSpc )
                z = complex(x,y)
                c = z
                iter = 1
                while True:
                    if abs(z) > self.maxRad or iter >= self.maxIter:
                        break
                    z = z**2 + c
                    iter += 1
                self._image[yindex-1][xindex-1] = iter

    def extract_df():
        pass

    @property
    def image(self):
        return self._image
