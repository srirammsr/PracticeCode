import pandas
#for i in range(1,10,5):
 #   print(i)

Fruits=['Grapes','Mangoes','Banana','Sapota']
print(len(Fruits))
print(Fruits[:2]) #first 2 items
print(Fruits[:-1]) #first 3 items
print(Fruits[-1]) 
print(Fruits[0:2])
print(Fruits[1:-1])
print(Fruits[:-3]) #first 3 items
print(Fruits[3])
print(sorted("Python"))
var1="aaaa bb ccc"
print(sorted(var1.split(), key=len))