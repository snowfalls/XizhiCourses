import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"distributions")))
x=np.random.normal(size=100)
sns.kdeplot(x)
sns.kdeplot(x,bw_method=1,label='bw1',legend=True)
sns.kdeplot(x,bw_method=2,label='bw2',legend=True) #???
plt.show()