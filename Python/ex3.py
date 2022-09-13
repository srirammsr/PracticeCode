import pandas as pd
df=pd.read_csv('E:\Downloads\RepPivot.csv')
print(df.columns)

#applying Lambda with dataframe
printthese=lambda x:print(df[x])
print(printthese('VirtualLocationID'))

#simple way
mx=lambda x,y:x if x>10 else y+10
print(mx(10,99))

#using map
# you can apply a formula for each element in the list.

var1=[1,2,3,4]
print(list(map(lambda x:2*x -3,var1)))

var1=(1,72,3,4)
print(tuple(map(lambda x:2*x -3,var1)))

# or
print([2*x-3 for x in var1])
print(type(var1))

#using filter
print(list(filter(lambda x:x>10,var1)))
