# The following python class is very improper way of writing code. It works though.
#I have created another file where the class a constructor and methods.
class products:
    pass
p1=products()
p2=products()

print(p1,p2)

p1.id=1001
p1.pname="Books"
p1.itemcost=50
p1.qty=20

p2.id=1021
p2.pname="Pens"
p2.itemcost=22
p2.qty=10

print(p1.pname)
print(p2.pname)
