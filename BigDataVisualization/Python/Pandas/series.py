import pandas as pd 
import numpy as np 
from pandas import DataFrame,Series 
import matplotlib.pyplot as plt 
from numpy.random import randn

s = pd.Series(randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
plt.show()