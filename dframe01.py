import pandas as pd
marksUT= {'Name':['Raman','Raman','Raman','Zuhaire','Zuhaire','Zuhaire', 'Ashravy','Ashravy','Ashravy','Mishti','Mishti','Mishti'],
 'UT':[1,2,3,1,2,3,1,2,3,1,2,3],
 'Maths':[22,21,14,20,23,22,23,24,12,15,18,17],
 'Science':[21,20,19,17,15,18,19,22,25,22,21,18],
 'S.St':[18,17,15,22,21,19,20,24,19,25,25,20],
 'Hindi':[20,22,24,24,25,23,15,17,21,22,24,25],
 'Eng':[21,24,23,19,15,13,22,21,23,22,23,20]
 }
df=pd.DataFrame(marksUT)
print("\n Dataframe result: \n",df)

print("\n Selecting Max Values: \n", df.max())

print("\n Selecting Max Numeric only Values: \n", df.max(numeric_only=True))

dfUT2 = df[df.UT == 2] # Result of Unit Test 2
print('\nResult of Unit Test 2:\n\n',dfUT2)
print('\n Maximum Mark obtained in Each Subject in Unit Test 2: \n\n',dfUT2.max(numeric_only=True))
print('\n Maximum Mark obtained in Each Subject in Unit Test 2: \n\n',df.max(axis=1))
print('\n Minimum Mark obtained in Each Subject in Unit Test 2: \n\n',df.min())
dfMishti = df.loc[df.Name == 'Mishti'] # minimum marks score by Mishti
print('\nMinimum Marks obtained by Mishti in each subject across the unit tests \n\n',dfMishti[['Maths','Science','S.St','Hindi','Eng']].min())
print('\nMaximum Marks obtained by Mishti in each subject across the unit tests \n\n',dfMishti[['Maths','Science','S.St','Hindi','Eng']].max())