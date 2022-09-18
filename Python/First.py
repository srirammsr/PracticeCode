import pandas as pd
df=pd.read_csv('E:\Downloads\RepPivot.csv',parse_dates=['Timeframe'], dayfirst=True,index_col='Timeframe')
print(df)
#print(len(df))
#print(df.columns)
print(df[['EmployeeID', 'MetricID']])
#plotting a column
print(df['MetricID'])

# How many ways we can write dictionaries 
# Method 1
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Method 2
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value
del phonebook["John"] #  or phonebook.pop("John")
print(phonebook)

# checking if a particular key is listed in dictionary, 
if "Jack" in phonebook:  
    print("Jack is listed in the phonebook")
    print(dir(pd))

