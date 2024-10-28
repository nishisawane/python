import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('marks.csv')
df= pd.DataFrame(data)
df.plot(kind='bar')
#set title,xlabel,ylabel
plt.title('Performance Analysis')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()