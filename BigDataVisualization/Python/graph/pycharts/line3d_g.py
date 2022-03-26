from pyecharts import Line3D
data = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
line3D = Line3D("3D图例",width=1000,height=1000)
line3D.add("",data,is_visualmap=True)
line3D.render()