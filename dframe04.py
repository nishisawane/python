import pandas as pd

marksUT= {'Name':['Raman','Raman','Raman','Zuhaire','Zuhaire','Zuhaire', 'Ashravy','Ashravy','Ashravy','Mishti','Mishti','Mishti'],
 'UT':[1,2,3,1,2,3,1,2,3,1,2,3],
 'Maths':[22,21,14,20,23,22,23,24,12,15,18,17],
 'Science':[21,20,19,17,15,18,19,22,25,22,21,18],
 'S.St':[18,17,15,22,21,19,20,24,19,25,25,20],
 'Hindi':[20,22,24,24,25,23,15,17,21,22,24,25],
 'Eng':[21,24,23,19,15,13,22,21,23,22,23,20]
 }
df = pd.DataFrame(marksUT)
print("Student Result - Dataframe : \n",df) # print all student result 
#Program 3-8 Write the statement to display the first and third quartiles of all subjects
dfSubject=df[['Maths','Science','S.St','Hindi','Eng']]
print("Marks of all the subjects:\n",dfSubject)
# First and third quartiles of all the subjects:
dfQ=dfSubject.quantile([.25,.75])
print("First and third quartiles of all the subjects:\n",dfQ)
# CALULATING VARIANCE 
print('\n Variance: \n', df[['Maths','Science','S.St','Hindi','Eng']].var())
#caclulating std. deviance
print('\n Std. deviance: \n', df[['Maths','Science','S.St','Hindi','Eng']].std())
print('\n Descrptive values : \n', df.describe())
