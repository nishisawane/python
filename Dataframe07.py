# (A) Adding a New Column to a DataFrame

import pandas as pd

ResultSheet={
'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])
}
ResultDF = pd.DataFrame(ResultSheet)
print(ResultDF) # print all student result 

# Adding a New Column to a DataFrame
ResultDF['Preeti']=[89,78,76]
print("\n Adding Preeti to result: \n", ResultDF) 
print("\n Result of Arnab: \n", ResultDF.Arnab) # print result of Arnab
#sets marks=90 for all subjects for the column name 'Arnab'
ResultDF['Arnab']=90
print("\n Setting Arnab's all subjects marks to 90:\n", ResultDF)
#Adding a New Row to a DataFrame
ResultDF.loc['English'] = [85, 86, 83, 80, 90, 89]
print("\n Adding extra English marks to all : \n",ResultDF)
# Setting all Maths marks to 50"
ResultDF[: ] = 60
print("\n Setting all subjects marks = 60 to all : \n",ResultDF)

