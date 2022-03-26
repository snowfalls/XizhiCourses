import matplotlib.pyplot as plt

x=[2012,2013,2014,2015,2016,2017,2018,2019,2020]
y=[53.9,59.3,64.1,68.6,74.0,82.1,90.0,98.7,101.6]
plt.plot(x, y)
plt.title("China's GDP from 2012 to 2020")
plt.xlabel("year")
plt.ylabel("GDP(trillion RMB)")
plt.show()