import numpy as np 
from bokeh.plotting import figure, output_file, show

output_file("sincos.html")
x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)
z=np.cos(x)
p=figure(plot_width=400,plot_height=400)
p.line(x,y)
p.line(x,z)
show(p)