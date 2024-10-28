# creation of dataframe
#(C) Creation of DataFrame from List of Dictionaries
import numpy as np
import pandas as pd

listDict = [{'a':10, 'b':20}, {'a':5,'b':10, 'c':20}]
dFrameListDict = pd.DataFrame(listDict)
print(dFrameListDict)