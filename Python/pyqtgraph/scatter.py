import pyqtgraph as pg
import numpy as np
pg.setConfigOption('background', 'w')
x=np.random.normal(size=100)
y=np.random.normal(size=100)
pg.plot(x,y,symbol='o')
input()