from bokeh.plotting import figure,output_file,show
output_file("render.html")
p=figure(plot_width=400, plot_height=400)
p.square([1,2,3,4,5],[7,8,5,3,7],size=30,color="red",alpha=0.5)
show(p)