import pyqtgraph as pg
import numpy as np
app = pg.mkQApp()
x=np.linspace(0,1*np.pi,100)
y=np.sin(x)
pg.plot(x,y)
app.exec_()