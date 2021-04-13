import numpy as np 
from bokeh.plotting import figure, output_file, show

output_file("patch.html")
p=figure(plot_width=400,plot_height=400)
p.patch([1,3,5],[5,8,5], alpha=0.5,line_width=2)
p.patch([2,3,4],[5.5,7,5.5],alpha=0.3,line_width=2)
show(p)