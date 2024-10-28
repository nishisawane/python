
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

print("\n Student Result slice Maths to Science : \n",ResultDF.loc['Maths':'Science'])

print("\n Student Result slice Maths to Science for Arnab : \n",ResultDF.loc['Maths':'Science','Arnab'])

print("\n Student Result slice Maths to Science for Arnab to Samridhi: \n",ResultDF.loc['Maths':'Science','Arnab':'Samridhi'])

print("\n Student Result: \n",ResultDF.loc[[True, False, True]])
