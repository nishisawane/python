import pandas as pd
marks = pd.read_csv("C:/infopractice/data.csv",sep =",", header=0)
print(marks)

marks1 = pd.read_csv("C:/infopractice/data.csv",sep=",",header=0,names=['RNo','StudentName', 'Sub1', 'Sub2'])
print("\n\n Header changes \n",marks1)

marks1.to_csv(path_or_buf='C:/infopractice/data1.csv', sep=',') 
print("\n\n Created CSV file as data1.csv \n")

marks1.to_csv('C:/infopractice/data1.txt',sep = ' ', header = False, index= False)
print("\n\n Created TXT file as data1.txt \n")
