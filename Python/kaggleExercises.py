#BEDMAS rule........ Brackets, Exponents, Division,Multiplication,Addition,Subtraction
from xmlrpc.client import boolean


print(5-3/2)
print(5**2) # 2 * means exponent. result:25
print(5**2-5) # first exponent is evaluated followed by subtraction.
print(round(2.65865,2))

def least_difference(a,b,c):
    diff1=a-b
    diff2=b-c
    diff3=c-a
    return min(diff1,diff2,diff3)

print(least_difference(100,220,300))
l=[33,144,55]
l.sort()
print(sum(l)/len(l))
