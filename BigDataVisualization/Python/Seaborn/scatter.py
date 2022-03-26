import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"distributions")))
mean,cov=[0,1],[(1,3.5),(3.5,1)]
data=np.random.multivariate_normal(mean,cov,200)
df=pd.DataFrame(data,columns=["x","y"])
with sns.axes_style("ticks"):
    sns.jointplot(x="x",y="y",data=df)
plt.show()