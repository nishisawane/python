# Accessing element of series USING INDEX
import pandas as pd
seriesCapCntry = pd.Series(['NewDelhi','WashingtonDC', 'London', 'Paris'], 
index=[10,20,30,40])
df1=seriesCapCntry
df2=seriesCapCntry[30]
print(df1) # SHOW THE SERIES
print(df2) # SHOWS THE INDEX POSITION