import numpy as np
import matplotlib.pyplot as plt

def plot_image(img, figsize=(4,4)):
    fig = plt.figure(figsize=figsize)
    plt.imshow(img)
    plt.show()

def plot_iterations(df, xindex, yindex, figsize=(8,12),
                    fxns=[np.real, np.imag, np.abs, np.angle],
                    cols=['blue', 'red', 'green', 'purple'],
                    fxn_names=['real', 'imag', 'abs', 'arg']):
    fig = plt.figure(figsize=(12,8))
    for pair in zip(fxns, cols):
        colName = 'Z.' + str(xindex) + '_' + str(yindex)
        plt.plot(df.index, df[colName].apply(pair[0]),
                 c=pair[1], marker='o')
    plt.legend(fxn_names)
    plt.show()

def plot_orbit(df, xindex, yindex):
    colName = 'Z.' + str(xindex) + '_' + str(yindex)
    fig = plt.figure(figsize=(4,4))
    plt.plot(df[colName].apply(np.real), df[colName].apply(np.imag))
    plt.show()
