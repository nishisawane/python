import pandas as pd
import matplotlib.pyplot as plt
data = {'Name':['Arnav', 'Sheela', 'Azhar', 'Bincy', 'Yash', 
'Nazar'], 
'Height' : [60,61,63,65,61,60], 
'Weight' : [47,89,52,58,50,47]
}
df=pd.DataFrame(data)
df.plot(kind='hist')
plt.show()