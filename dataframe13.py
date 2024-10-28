# 2.3.5 Joining, Merging and Concatenation of 

import pandas as pd

dFrame1=pd.DataFrame([[1, 2, 3], [4, 5],[6]], columns=['C1','C2','C3'], index=['R1','R2','R3'])
print(" Dataframe result : \n",dFrame1)

dFrame2=pd.DataFrame([[10, 20], [30], [40, 50]], columns=['C2','C5'], index=['R4','R2','R5'])
print('\n Dataframe result: \n', dFrame2)

dFrame3=dFrame1.append(dFrame2)
print('\n Dataframe result : \n',dFrame3)

# append dFrame1 to dFrame2 
dFrame4 =dFrame2.append(dFrame1,sort='True')
print("\n Dataframe result : \n",dFrame4)

dFrame5 = dFrame1.append(dFrame2, ignore_index=True)
print("\n Dataframe result : \n",dFrame5)
