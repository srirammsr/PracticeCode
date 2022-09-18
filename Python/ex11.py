import pandas as pd
import math
df=pd.read_csv('E:\Downloads\RepPivot.csv',index_col ='EmployeeID')
print(df.columns)
#print(df['MetricID'].unique());#print(df['MetricID'].head());#print(df['Result_Num'].mean());#print(df['Result_Num'].median())
#print('Sum of Result_num is: ',df['Result_Num'].sum())

#df_Salaries=pd.DataFrame({'Salaries':[23453,67867,67432,96753,97990,math.nan],'comm':[23.23,56,34,35.75,12,67]})
#print(df_Salaries); print('\n Median of salaries and Commision are :\n',df_Salaries.median())
print(df.loc['MetricID'])
