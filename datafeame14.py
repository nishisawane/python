# 2.3.6 Attributes of DataFrames
import pandas as pd

ForestArea = {
 'Assam' :pd.Series([78438, 2797, 10192, 15116],
          index = ['GeoArea', 'VeryDense','ModeratelyDense', 'OpenForest']),
          'Kerala' :pd.Series([ 38852, 1663,9407, 9251],
           index = ['GeoArea' ,'VeryDense', 'ModeratelyDense', 'OpenForest']),
           'Delhi' :pd.Series([1483, 6.72, 56.24,129.45], 
            index = ['GeoArea', 'VeryDense','ModeratelyDense', 'OpenForest'])}
ForestAreaDF = pd.DataFrame(ForestArea)
print("\n Forest Area : \n", ForestAreaDF)

