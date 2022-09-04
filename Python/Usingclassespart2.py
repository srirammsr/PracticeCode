# usage of self is mandatory while defining methods in classes.
# any miss of self throws an error.

class Products:
    def __init__(self,pid,pname,rate,qty):
        self.pid=pid
        self.pname=pname
        self.rate=rate
        self.qty=qty
        self.Amount=rate*qty
    def print(self):
        print("Id        : ",self.pid,"\nProduct Name   : ",self.pname,"\nRate      : ",self.rate,"\nQuantity   :",self.qty,"\nTotal Amount :",self.Amount)
        print("******************************************************")
    def print2(self):
        print("PID:{} Product Name: {} Rate:{} Qty:{} Amount:{}\n".format(self.pid,self.pname,self.rate,self.qty,self.Amount))
    def print3(self):
        return "PID:{} Product Name: {} Rate:{} Qty:{} Amount:{}\n".format(self.pid,self.pname,self.rate,self.qty,self.Amount)


p1=Products(1001,"John",45,66)
p1.print()

p2=Products(1021,"Maven",15,6)
p2.print()

p1.print2()
p2.print2()

print(p1.print3())
print(p2.print3())