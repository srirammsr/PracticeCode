import math

#**********************************************************
# import numpy as np 
# can also be written as

# import numpy
# np=numpy
#**********************************************************

print(math.pi)

print("It's math! It has type {}".format(type(math)))

# We can see all the names in math using the built-in function dir()
print(dir(math))

#We can access these variables using dot syntax. Some of them refer to simple values, like math.pi:
print(math.pi)
print(math.tan(45))
print("pi to 3 significant digits = {:.3}".format(math.pi))
print("={:.3}".format(math.log(30,2)))

# use help to find more details about the function. Example:
print(help(math.log))

# if we could just refer to pi instead of math.pi then use the following import statement
# from math import *        --these kind of import can be used only if there is only 1 import line in 
#                             the entire file. Sometimes a conflict migyht arise if 2 imports are used.
# ex:
# print(pi)

# you can import specific functions in this form:
# from math import log, pi
# from numpy import asarray
import numpy 
print('numpy.random is a ',type(numpy.random))
print('the members of random module are {}'.format(dir(numpy.random)))
print('15 members of random module are {}'.format(dir(numpy.random)[0:15]))  # to list only 15 of them 

print(numpy.random.randint(low=1,high=6,size=5))
print(type(numpy.random.randint(low=1,high=6,size=5)))
rolls=numpy.random.randint(low=1,high=6,size=5)
print(rolls.mean())
rolls=rolls.tolist()
print(type(rolls))

