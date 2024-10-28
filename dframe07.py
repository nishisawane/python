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
#Sorting By default, sorting is done in ascending order. 
print('\n Sort by name : \n',df.sort_values(by=['Name']))
dfUT2 = df[df.UT == 2]
print('\n Data \n', dfUT2) # to obtain sorted list of marks scored by all students in Science in Unit Test 2,
# Sort according to ascending order of marks in Science Chapter 3.indd 77 11/26/2020 12:46:04 PM 2022-23 78 Informatics Practices
print('Marks : \n', dfUT2.sort_values(by=['Science']))