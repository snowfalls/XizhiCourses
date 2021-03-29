import pyqtgraph as pg
import numpy as np
x=np.random.normal(size=100)
y=np.random.normal(size=100)
pg.plot(x,y,pen=None,symbol='o')
input()