import pandas as pd
df=pd.read_csv('C:\\Users\\srira\\OneDrive\\Documents\\MyDocs.csv')
pd.options.display.max_columns =15
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', 35)
#print(df[df['Name']=='Mallavarapu Sri Ram Murthy'])
print(df)
#print(pd.set_option('display.max_columns',30))
#print(df.describe(),df.info())
