import numpy as np
import Mandelbrot as m
import matplotlib.pyplot as plt
import PlotUtils as p

# Setup
f1 = m.Mandelbrot()
f1.setup()

# Extract df and plot iteration orbits
#df_m = f1.extract_df()
#p.plot_iterations(df_m, 30, 34)

# Create and plot image of fractal
f1.calc_image()
arr = f1.image
p.plot_image(arr)
