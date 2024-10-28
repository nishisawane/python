# Accessing element by slicing using NumPy series 
import pandas as pd
# slicing in numpy
import numpy as np
seriesAlph = pd.Series(np.arange(10,16,1), 
index = ['a', 'b', 'c', 'd', 'e', 'f'])
ss = seriesAlph
print(ss)

# now index range slicing
seriesAlph['a':'c'] = 500
ss1= seriesAlph
print(ss1)