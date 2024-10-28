import pandas as pd
S = pd.Series([4300, 6500, 3900, 6100])
S.update(pd.Series([3400,6500,5000,5000]))
print(S)