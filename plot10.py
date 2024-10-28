import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('minmaxtemp.csv',usecols=['ANNUAL - MIN'])
df=pd.DataFrame(data)
#convert the 'ANNUAL - MIN' column into a numpy 1D array
minarray=np.array([df['ANNUAL - MIN']])
# Extract y (frequency) and edges (bins)
y,edges = np.histogram(minarray)
#calculate the midpoint for each bar on the histogram
mid = 0.5*(edges[1:]+ edges[:-1])
df.plot(kind='hist',y='ANNUAL - MIN', plt.plot(mid,y,'-^'))
plt.title('Annual Min Temperature plot(2000 - 2009)')
plt.xlabel('Temperature')
plt.show()