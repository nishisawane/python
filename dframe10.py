import pandas as pd
data={'Store':['S1','S4','S3','S1','S2','S3','S1','S2','S3'],
      'Year':[2016,2016,2016,2017,2017,2017,2018,2018,2018],
      'Total_sales(Rs)':[12000,330000,420000, 20000,10000,450000,30000, 11000,89000],
      'Total_profit(Rs)':[1100,5500,21000,32000,9000,45000,3000,1900,23000]
      }
df=pd.DataFrame(data)
print('\n Sales : \n',df)
# will get the data related to store S1
S1df = df[df.Store=='S1']
print('\n Data related to store S1: \n', S1df)
#find the total of sales for Store S1
print('\n The total of sales for Store S1 : \n', S1df['Total_sales(Rs)'].sum())

#will get the data related to store S3
S3df = df[df.Store=='S3']
print('\n Data related to store S3: \n', S3df)

#find the maximum sale for Store S3
S3df['Total_sales(Rs)'].max()
print('\n The maximum sales for Store S3 : \n', S3df['Total_sales(Rs)'].max())