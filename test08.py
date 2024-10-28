import pandas as pd
import matplotlib.pyplot as plt
data = {'year':[1960,1970,1980,1990,2000,2010], 
'paki_pop' : [44.91, 58.09, 78.07, 107.7, 138.5, 170.6],
'indi_pop' : [449.48, 553.57, 696.783, 870.133, 1000.4,1309.1]
}
df=pd.DataFrame(data)
df.plot(kind='line')
plt.title('Population Performance Analysis')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.show()
