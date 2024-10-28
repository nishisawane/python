# Addition of series.
import numpy as np
import pandas as pd
seriesA = pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e'])
seriesB = pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e'])
print(seriesA)
print(seriesB)
print(seriesA+seriesB)
print("Series Addition: \n",seriesA.add(seriesB, fill_value=0)) # series addition
print ("Series subtraction: \n", seriesA.subtract(seriesB)) # series substraction
print("Series multiplication: \n",seriesA.multiply(seriesB)) # series multiplication
print("Series Division: \n",seriesA.divide (seriesB)) # series division
print("Placed 0 instead Nan: \n",seriesA.mul(seriesB, fill_value=0)) # zero placed instead NaN