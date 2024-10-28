# 2.3.3 Accessing DataFrames Element through Indexing - Label based index

import pandas as pd

ResultSheet={
'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])
}
ResultDF = pd.DataFrame(ResultSheet)
print("Student Result - Dataframe : \n",ResultDF) # print all student result 

print("\n Students science & Hindi marks: \n",ResultDF.loc[['Science','Hindi']]) # print all student result 
