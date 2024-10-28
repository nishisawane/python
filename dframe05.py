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
print("Student Result : \n",df) # print all student result 

print("Data aggregation Result with count: \n",df.aggregate(['max','count'])) # data agreegation 

print("Maths data max & min marks : \n", df['Maths'].aggregate(['max','min'])) # data max/min for maths 
#Total marks of Maths and Science obtained by each student.
#Use sum() with axis=1 (Row-wise summation)
print('\n Total marks of Maths and Science obtained by each student: \n', df[['Maths','Science']].aggregate('sum',axis=1))

