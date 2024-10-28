# The following example shows that we can use letters or strings as indices:
import numpy as np 
import pandas as pd
array1 = np.array([1,2,3,4])
series3 = pd.Series(array1)
series4 = pd.Series(array1, index = ["Jan","Feb", "Mar", "Apr"])
print(series4)