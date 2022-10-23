import pandas as pd
import math
df=pd.read_csv('E:\Excercises\Dataset\SampleSuperstore.csv', encoding = 'utf8')
print(df.columns)
print(df['Ship Mode'].unique());print(df['State'].head());print(df['Sales'].mean());print(df['Profit'].median())
print('Sum of Profit is: ',df['Profit'].sum())

#df_Salaries=pd.DataFrame({'Salaries':[23453,67867,67432,96753,97990,math.nan],'comm':[23.23,56,34,35.75,12,67]})
#print(df_Salaries); print('\n Median of salaries and Commision are :\n',df_Salaries.median())
print('Extracting 0th and 1st row using df.iloc[0:2] \n',df.iloc[0:2]  )
print('LIsting 2 columns df[[\'Ship Mode\',\'Segment\']]\n',df[['Ship Mode','Segment']])
var_shipmode='Standard Class'
var_sales=1500
seg='Corporate'

#print(df[df['Sales']>1500])

df_new=df.query('Sales >@var_sales and Segment==@seg')
print(df_new)

# to find n large sales rows
print(df.nlargest(4,'Sales'))

# to find n small sales values
print(df.nsmallest(4,'Sales'))

#print(df)

#Another example
df2 = pd.DataFrame({"var1": ["AA_2", "B_1", "C_2", "A_2"]})
print(df2)
#print(df2[df2['var1'].str[0] == 'A'])   #first letter is A
print(df2[df2['var1'].str.contains('AA')]) # contains AA
print(df2[df2['var1'].str.startswith('AA')]) # begins with AA
print(df2[df2['var1'].str.endswith('2')]) # ends with 2


