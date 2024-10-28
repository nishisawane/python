import pandas as pd
#Create Dictionary
df1= {
    "round":[1,2,3,4],
    "P1":[700,975,970,900],
    "P2":[490, 460, 570,590]
        }
#Create Dataframe
df_1=pd.DataFrame(df1)
print(df1)
df2= {
    "round":[1,2,3,4],
    "P1":[1100,1275,1270,1400],
    "P2":[1400, 1260, 1500,1190]
}

df_2=pd.DataFrame(df2)
df_2['TotalPoint']=df_2["P1"]+df_2["P2"]
df_2[["TotalPoint"]]
print(df_2)