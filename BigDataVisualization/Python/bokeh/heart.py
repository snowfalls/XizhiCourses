from bokeh.plotting import figure,output_file,show
import numpy as np

p=figure(plot_width=400, plot_height=400)
x = np.linspace(-8, 8, 1024)
y1 = 0.618 * np.abs(x) - 0.8 *  np.sqrt(64 - x**2)
y2 = 0.618 * np.abs(x) + 0.8 *  np.sqrt(64 - x**2)
p.line(x, y1, line_width=2, color='red')
p.line(x, y2, line_width=2, color='red')
show(p)