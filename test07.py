import pandas as pd
import matplotlib.pyplot as plt
data = {'product':['TV', 'FRIDGE', 'AC'], 
'qtr1' : [2000000, 300000, 240000],
'qtr2' : [230000, 200000, 153000],
'qtr3' : [210000, 290000, 245000],
'qtr4' : [240000, 210000, 170000]
}
df=pd.DataFrame(data)
print(df)
df.drop([1], axis=0, inplace=True)
print(df)
