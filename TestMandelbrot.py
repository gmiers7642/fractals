import numpy as np
import Mandelbrot as m
import matplotlib.pyplot as plt
import PlotUtils as p

f1 = m.Mandelbrot()
f1.setup()
df_m = f1.extract_df()

p.plot_iterations(df_m, 30, 34)
