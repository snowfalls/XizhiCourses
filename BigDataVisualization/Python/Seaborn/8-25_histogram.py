import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"distributions")))
x=np.random.normal(size=100)
sns.displot(x,kde=True,bins=20,rug=True)
# sns.displot(x,kde=True,bins=20,rug=False)
plt.show()