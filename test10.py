import pandas as pd
import matplotlib.pyplot as plt

d1={'Year':[2000,2002,2004,2006,2008,2010,2012,2014,2016,2018],
    'Production':[4,6,7,15,24,2,19,5,16,4]}
df1 =pd.DataFrame(d1)
plt.title('Yearwise wheat production')
plt.xlabel('Year')
plt.ylabel('Production')
df1.plot.hist()
plt.show()
