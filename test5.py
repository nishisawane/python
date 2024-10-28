import pandas as pd
import matplotlib.pyplot as plt
data1 = {'P1':[700,975,970,900],'P2':[490,460,570,590]}
data2 = {'P1':[1100,1275,1270,1400],'P2':[1400,1260,1500,1190]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)

df_murged = df1.merge(df2)
print(df_murged)
