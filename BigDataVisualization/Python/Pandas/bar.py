import pandas as pd 
import numpy as np 
from pandas import DataFrame,Series 
import matplotlib.pyplot as plt 
from numpy.random import randn,rand

fig,axes=plt.subplots(2,1)
df=pd.Series(rand(16),index=list('abcdefghijklmnop'))
df.plot.bar(ax=axes[0], color='r', alpha=0.7)
df.plot.barh(ax=axes[1], color='r', alpha=0.7)
plt.show()