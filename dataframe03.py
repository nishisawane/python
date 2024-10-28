# (D) Creation of DataFrame from Dictionary of Lists
import pandas as pd

dictForest = {'State': ['Assam','Delhi','Kerala'],'GArea':[78438,1483,38852],'VDF':[2797,6.72,1663]}
dFrameForest= pd.DataFrame(dictForest)
print(dFrameForest)

dFrameForest2 = pd.DataFrame(dictForest,columns = ['State','VDF','GArea'])
print(dFrameForest2)
 