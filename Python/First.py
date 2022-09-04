import pandas as pd
df=pd.read_csv('E:\Downloads\RepPivot.csv',parse_dates=['Timeframe'], dayfirst=True,index_col='Timeframe')
print(df)
#print(len(df))
#print(df.columns)
print(df[['EmployeeID', 'MetricID']])
#plotting a column
print(df['MetricID'].NaN())