# (D) Renaming Row Labels of a DataFrame

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

# deleting Science subject (row) from dataframe
ResultDF=ResultDF.rename({'Maths':'Sub1','Science':'Sub2','English':'Sub3','Hindi':'Sub4'}, axis='index')
print("\n Renamed subjects as follow: \n", ResultDF)

# (E) Renaming Column Labels of a DataFrame except Riya
ResultDF=ResultDF.rename({'Arnab':'Student1','Ramit':'Student2','Samridhi':'Student3','Mallika':'Student4'},axis='columns')
print("\n Renamed student names as follows: \n", ResultDF)
