from bokeh.plotting import figure,output_file,show
output_file("render.html")
p=figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5],[3,4,5,6,7],size=20,color="red",alpha=0.5)
show(p)