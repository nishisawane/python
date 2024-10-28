# Accessing element by slicing series 
import pandas as pd
seriesCapCntry = pd.Series(['NewDelhi','WashingtonDC', 'London', 'Paris'], 
index=['India','USA', 'England', 'France'])
df1=seriesCapCntry
df2=seriesCapCntry[1:3]
print(df1) # SHOW THE SERIES
print(df2) # SHOWS THE slicing POSITION