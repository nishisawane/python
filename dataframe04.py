# (F) Creation of DataFrame from Series
import pandas as pd

seriesA = pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e'])
seriesB = pd.Series ([1000,2000,-1000,-5000,1000], index = ['a', 'b', 'c', 'd', 'e'])
seriesC = pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e'])

dFrame6 = pd.DataFrame(seriesA) #We can create a DataFrame using a single series
print(dFrame6)
dFrame7 = pd.DataFrame([seriesA, seriesB, seriesC]) #We can create a DataFrame using multiple series
print("Multiple series :\n", dFrame7)
dFrame8 = pd.DataFrame([seriesA, seriesC])
print("Multiple series :\n", dFrame8) # we can make & print the multiple series