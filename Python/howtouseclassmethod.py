class A:
    newprice  =1.6
    def __init__(self,qty,rate):
        self.qty=qty
        self.rate=rate
    def listvalues(self):
        print(self.__dict__)
    @classmethod
    def doubleRate(cls,newvalue):
        cls.newprice=newvalue

#Using classmethod, value of a variable changed through class or its instance reflects across all instances
A.doubleRate(1.1)
p1=A(10,3)
p1.listvalues()

print(A.newprice)
print(p1.newprice)

# even instance variables too can access classmethods. Lets use the classmethod with instance variable and see
p1.doubleRate(13)
print(A.newprice, "\n", p1.newprice)

