from bokeh.plotting import figure,output_file,show
output_file("render.html")
p=figure(plot_width=400, plot_height=400)
p.patch([1,2,3,4,5],[6,8,5,3,4],alpha=0.5,line_width=2)
show(p)