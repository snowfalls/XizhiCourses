import pandas as pd 
import numpy as np 
from pandas import DataFrame,Series 
import matplotlib.pyplot as plt 
from numpy.random import randn,rand

df = pd.DataFrame(rand(4,4),columns= pd.Index(['A','B','C','D'],name='bar'),index=['one','two','three','four'])
df.plot.bar()
plt.show()