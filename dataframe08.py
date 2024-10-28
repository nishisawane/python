# (C) Deleting Rows or Columns from a DataFrame

import pandas as pd

ResultSheet={
'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])
}
ResultDF = pd.DataFrame(ResultSheet)
print("Student Result : \n",ResultDF) # print all student result 

# deleting Science subject (row) from dataframe
ResultDF = ResultDF.drop('Science', axis=0)
print("\n Deleted science (row) : \n", ResultDF)

# deleting Students (columns) from dataframe
ResultDF = ResultDF.drop(['Samridhi','Ramit','Riya'], axis=1)
print("\n Deleted students Samridhi, Ramit & Riya (columns) : \n", ResultDF)