import pandas as pd
import matplotlib.pyplot as plt
#read the CSV file in 'data'
data = pd.read_csv('compareresort.csv')
#convert 'data' into a DataFrame 'df'
df=pd.DataFrame(data)
#plot a box plot for the DataFrame 'df' with a title
df.plot(kind='box',title='Compare Resorts')
#set xlabel,ylabel
plt.xlabel('Resorts')
plt.ylabel('Rating (5 years)')
#display  
plt.show()