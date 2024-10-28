import pandas as pd
import numpy as np
seriesTenTwenty=pd.Series(np.arange(10,20,1))
print(seriesTenTwenty)
print(seriesTenTwenty.head(2)) # first 2 entries
print(seriesTenTwenty.tail(2)) # last 2 entries
print(seriesTenTwenty.tail()) # last 3 entries