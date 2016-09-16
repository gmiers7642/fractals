import numpy as np
import matplotlib.pyplot as plt

def plot_iterations(df, xindex, yindex, figsize=(8,12),
                    fxns=[np.real, np.imag, np.abs, np.angle],
                    cols=['blue', 'red', 'green', 'purple'],
                    fxn_names=['real', 'imag', 'abs', 'arg']):
    fig = plt.figure(figsize=(12,8))
    for pair in zip(fxns, cols):
        colName = 'Z.' + str(yindex) + '_' + str(xindex)
        plt.plot(df.index[2:] - 2, df[colName].iloc[2:].apply(pair[0]),
                 c=pair[1], marker='o')
    plt.legend(fxn_names)
    plt.show()
