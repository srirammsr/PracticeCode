from io import StringIO 
import pandas as pd
data = ('col1,col2,col3\n a,b,3\n c,d,6\n w,e,4')
df=pd.read_csv(StringIO(data),delimiter=',')
df_OddRowsOnly=pd.read_csv(StringIO(data),delimiter=',',skiprows=lambda x:x%2!=0)
print(df)
print(df_OddRowsOnly)

dfexcel=pd.read_excel('E:\Downloads\sample.xlsx',skiprows=lambda x:x%2!=0)  #skiprows parameter ensures that only even rows are stored in dfexcel
dfexcel=pd.read_excel('E:\Downloads\sample.xlsx',converters={'Amount':int})

print(dfexcel)
print(dfexcel['Sales Person'][1])
print(dfexcel['Country'][1])
print(dfexcel['Amount'].max())