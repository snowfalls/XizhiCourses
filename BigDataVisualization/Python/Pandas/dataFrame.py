import pandas as pd 
import numpy as np 
from pandas import DataFrame,Series 
import matplotlib.pyplot as plt 
from numpy.random import randn

df = pd.DataFrame(randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
df.plot()
plt.show()