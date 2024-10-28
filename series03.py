# Here, data values Kavi, Shyam and Ravi have index values 3, 5 and 1, 
# respectively. We can also use letters  or strings as indices, for example

import pandas as pd
series2 = pd.Series([2,3,4],index=["Feb","Mar","Apr"])
print(series2)