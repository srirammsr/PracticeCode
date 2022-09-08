import pandas as pd 
df=pd.read_csv('E:\survey_results_public.csv')
pd.set_option('display.max_columns',85) #sets display width to 85 columns. More useful if you areusing Jupyter.
print(df)        #Prints entire dataset
print(df.shape) #returns rows by column details.
print(df.info())    #returns details of each column
print(df.columns) #returns Lists Columns
print(df.columns.str.capitalize()) #First letter of each column name capital
print(df.columns.str.upper()) #Lists Columns in uppercase.
print(df.head())
print(df.tail())