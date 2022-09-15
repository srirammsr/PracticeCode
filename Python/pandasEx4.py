import pandas as pd

listvar=['Apples','Bananas','grapes','Oranges']
df=pd.DataFrame(listvar)
print(df)

#using group of lists
listvar={'fruits':['Pomogranate','Bananas','grapes','Oranges'],
          'Stock':[22,343,44,55] , 
          'Sold':[6,222,20,33]
        }
df=pd.DataFrame(listvar)
print(type(listvar))    #printing the data type of listvar variable.

print(df)
print(df[['fruits', 'Sold']])   # printing 2 columns only.

# using csv file
df1=pd.read_csv('E:\\Downloads\\nba.csv',index_col='Name')
first=df1.loc['Shelvin Mack'] # print all column values pertaining to Name='Shelvin Mack'
print(first)

