import pandas as pd
import numpy as np

df=pd.read_csv('E:\Downloads\RepPivot.csv')
print(df.info())
print(df.shape)
print(df[0:2]) #top 2 rows
print(df.loc[0:2]) #top 3 rows......... 0,1,2nd rows
print(df[['EmployeeID','Timeframe']].head(11)) # 0 to 10 rows only. A total of 11
print(df.dtypes)    # lists the data types of each column

#different ways to declare a dataframe
print(df.count)

s=pd.Series([12,34,56,78,np.nan])
print(s)
print(s.max())
print(s.sum())

datevals=pd.date_range("2022-Mar-01",periods=6)
print(datevals)

dfnew=pd.DataFrame(np.random.randn(6,4),index=datevals,columns=list("ABCD"))
print(dfnew)

print(np.random.randint(1,4))


