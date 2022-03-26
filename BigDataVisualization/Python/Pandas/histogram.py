import pandas as pd 
import numpy as np 
from pandas import DataFrame,Series 
import matplotlib.pyplot as plt 
from numpy.random import randn,rand

df = pd.DataFrame({'a':randn(1000)+1,'b':randn(1000),},columns=['a','b'])
# df.plot.hist(bins=20)
df.plot.hist(bins=20,stacked=True)
plt.show()