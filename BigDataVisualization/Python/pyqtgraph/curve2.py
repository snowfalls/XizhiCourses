import pyqtgraph as pg
import numpy as np
app = pg.mkQApp()
x=np.random.randn(10)
pg.plot(x)
app.exec_()