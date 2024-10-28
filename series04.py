# Creation of Series from NumPy Arrays 
# We can create a series from a one-dimensional (1D) 
# NumPy array, as shown below: 

import numpy as np # import NumPy with alias np
import pandas as pd
array1 = np.array([1,2,3,4])
series3 = pd.Series(array1)
print(series3)