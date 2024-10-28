import pandas as pd
import matplotlib.pyplot as plt
d1 = {'student':['Ram', 'Shyam', 'Rama', 'Kashish', 'Mayant'], 
'Accountacy' : [87, 82, 99, 85, 80], 
'BusinessStudies' : [90, 79, 95, 93, 85]}
df=pd.DataFrame(d1)
df.plot(kind='bar', x='student')
plt.show()
