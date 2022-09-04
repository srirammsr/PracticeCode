#using class variables

class Products:
    new_price=1.2       #this is class variable
    def __init__(self,pid,pname,rate,qty):
        self.pid=pid
        self.pname=pname
        self.rate=rate
        self.qty=qty
        self.Amount=rate*qty
    def print(self):
        print("Id        : ",self.pid,"\nProduct Name   : ",self.pname,"\nRate      : ",self.rate,"\nQuantity   :",self.qty,"\nTotal Amount :",self.Amount)
        print("******************************************************")
    def newprice(self):
        self.Amount=self.Amount*Products.new_price   #new_price variable has to be accompanied by class variable.
        print("new price came into effect")
        

p1=Products(1111,"Toys",100,6)
p1.print()
print(p1.__dict__)
p1.newprice()
p1.print()




