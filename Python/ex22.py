import pandas as pd
df=pd.read_csv('E:\Excercises\Dataset\SampleSuperstore.csv', encoding = 'utf8')
##print(df)
print(df.columns)
print(list(df.groupby(by='Category')))
print(df['Category'].unique())