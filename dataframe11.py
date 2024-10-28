# (B) Boolean Indexing

import pandas as pd

ResultSheet={
'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])
}
ResultDF = pd.DataFrame(ResultSheet)
print("Student Result - Dataframe : \n",ResultDF ) # print all student result 

print("\n\n",ResultDF)
# print("\n Boolean index to check math marks > 90: \n",ResultDF.loc['Maths'] > 90) # Boolean print all student result 

# to check in which subjects ‘Arnab’ has scored more than 90, we can write:
# print("\n Boolean index to check Arnab's marks > 90: \n",ResultDF.loc[:,'Arnab']>90)