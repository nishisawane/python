import pandas as pd
S1=pd.Series([5,6,7,8,10], index=['v','w','x','y','z'])
l=[1,6,1,4,6]
S2=pd.Series(l,index=['z','y','a','w','v'])
print(S1)
print(S2)
print(S1-S2)