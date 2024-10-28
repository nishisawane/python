
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

# Create a GROUP BY Name of the student from DataFrame df
g1=df.groupby('Name')
#Displaying the first entry from each group
print('\n Grouping the data :\n', g1.first())
print('\n Grouping Size :\n', g1.size())

#Displaying group data, i.e., group_name, row indexes corresponding to the group and their data type 
g1.group={'Ashravy': (6, 7, 8), 'Mishti': (9, 10, 11),'Raman': (0, 1, 2), 'Zuhaire': (3, 4, 5)}
#Printing data of a single group
print('Grouping for Raman: \n',g1.get_group('Raman'))

