#select a random item from list

import random

cities_to_visit=('Hyderabad','Guntur','Vijaywada','Vizag')
print(random.choice(cities_to_visit))

#print random numbers
print(random.randint(10,100))
var=random.randint(10,100)
match var:
    case 10:
        print('hhahahah')
    case 20:
        print('hhahahah1111111111111')
    case default:
        print('else part reached')


cars = ["Aston", "Audi", "McLaren "]
for i, x in enumerate(cars):
    print(i,x)
for x in enumerate(cars):
    print(x[0],x[1])
for x in enumerate(cars, start=10):
    print(x[0],x[1])

carModels=['maruthi','Honda','Tata Tiago']
CarPrices=[500000,800000,400000]
zipped=list(zip(carModels,CarPrices))
print(zipped)
print(type(zipped))

import sys
print(sys.version)


