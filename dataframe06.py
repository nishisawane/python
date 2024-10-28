# When a DataFrame is created from a Dictionary of Series, the resulting index or row labels are a union of all 
# series indexes used to create the DataFrame.:

import pandas as pd

dictForUnion = { 'Series1' : 
pd.Series([1,2,3,4,5],index = ['a', 'b', 'c', 'd', 'e']) ,
 'Series2' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']),
 'Series3' : pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e']) 
 }
dFrameUnion = pd.DataFrame(dictForUnion)
print(dFrameUnion) # union of all the series above.

