import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'GeoArea':[83743,78438,22327,22429,21081,16579,10486],'ForestCover':[67353,27692,17280,17321,19240,13464,8073]}, 
index=['Arunachal Pradesh','Assam','Manipur','Meghalaya', 'Mizoram','Nagaland','Tripura'])
exp=[0.1,0,0,0,0.2,0,0] 
#explode the first wedge to .1 level and fifth to level 2. 
c=['r','g','m','c','brown','pink','purple']
#change the color of each wedge
df.plot(kind='pie',y='ForestCover',title='Forest cover of North Eastern states', legend=False, explode=exp, autopct="%.2f",colors=c)
plt.show()
