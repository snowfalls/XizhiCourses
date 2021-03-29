import numpy as np 
import pyqtgraph as pg
app=pg.mkQApp()
x=np.linspace(2,10*np.pi,100)
z=np.cos(x)
pg.plot(x,z)
app.exec_()