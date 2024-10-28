# Accessing element of series
import pandas as pd
seriesNum = pd.Series([10,20,30])
df = seriesNum[2]
print(df) # shows index postion 3 in series.

seriesCapCntry = pd.Series(['NewDelhi','WashingtonDC', 'London', 'Paris'], 
index=['India', 'USA', 'UK', 'France'])
df1=seriesCapCntry['India']
df2=seriesCapCntry[1]
df3=seriesCapCntry[['UK','USA']]
print(df1) # shows New Delhi 
print(df2) # shows the index position of series 
print(df3) # shows the values against index test

 