from bokeh.plotting import figure,output_file,show
output_file("render.html") #这句话放在程序中间不起作用，除非放在程序最后面，这样做是为了避免生成不用的html文件
p=figure(plot_width=400, plot_height=400)
p.patch([1,2,3,4,5],[6,7,8,9,10],alpha=0.5,line_width=2)
show(p)
