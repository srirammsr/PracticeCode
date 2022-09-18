import pandas as pd 
df=pd.read_csv('E:\survey_results_public.csv')
"""
pd.set_option('display.max_columns',85) #sets display width to 85 columns. More useful if you are using Jupyter.
print(df)        #Prints entire dataset
print(df.shape) #returns rows by column details.
print(df.info())    #returns details of each column
print(df.columns) #returns Lists Columns
print(df.columns.str.capitalize()) #First letter of each column name capital
print(df.columns.str.upper()) #Lists Columns in uppercase.
print(df['RemoteWork'].str.upper()) #prints particular column in upper case
print("Head............")
print(df.head())
print("tail.............")
print(df.tail())
"""
print("********************************")
print(df[1:3])

print(df[0:3])

print("********************************")

print(df[['ResponseId', 'MainBranch', 'Employment', 'RemoteWork']])
print(df.iloc[1:4,2:6]) #Display 1st row to 4th row AND 2nd column to 6th column'NOTE: The numbering starts from 0
print(df.iloc[:,0:4])   # print(df.iloc[2,1]).....this display cell in 2nd row and 1st row
print(df.iloc[:,0:4].drop_duplicates)

#print(df['MainBranch'][0:5])
#for i,x in df.iterrows():
 #   print(i,x)
#for i,x in df.iterrows():
#    print(i,x['ResponseId'])
#print((df['ResponseId']>73000) & (df['RemoteWork']=='Fully remote'))
#df.describe()
#print(df["ResponseId"].between(73000,73010))
print(df[(df['ResponseId'] >= 73268) & (df['ResponseId'] <= 73270)])

#df.ResponseId=73268



