# creation of dataframe
import numpy as np
import pandas as pd
array1 = np.array([10,20,30])
array2 = np.array([100,200,300])
array3 = np.array([-10,-20,-30, -40])
dFrame4 = pd.DataFrame(array1)
print(dFrame4)
# Dataframes from arrays with column name
dFrame5 = pd.DataFrame([array1, array3,array2], columns=[ 'A', 'B', 'C', 'D'])
print(dFrame5)