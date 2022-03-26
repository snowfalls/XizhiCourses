from bokeh.plotting import figure,output_file,show
import numpy as np

output_file("render.html")
x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)
p=figure(plot_width=400, plot_height=400)
p.line(x,y)
show(p)