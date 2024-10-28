import pandas as pd
import matplotlib.pyplot as plt
Maker ="*"
Markersize=10
linestyle="--" 
Linewidth =3
df=pd.read_csv("Melasales.csv") 
#creates plot of different color for each week
df.plot(kind='line',color=['red','blue','brown'],marker="*",markersize=10,linewidth=3,linestyle="--")
plt.title('Mela Sales Report')
plt.xlabel('Days') 
plt.ylabel('Sales in Rs')
#store converted index of DataFrame to a list
ticks = df.index.tolist()
#displays corresponding day on x axis
plt.xticks=(ticks,df.Day)
plt.show()