x = 10
y = "Python is fun"
z = 144 ** 0.5 == 12
print(x, y, z)

p = 10
a = x + z + p
print(a)

m = n = 4
print(m, n)

x, y, z = (10, 20, 30)
print(x, '|', y, '|', z)

x, y = y, x
print(x, y)

'''
When we assign a variable in python. the var is reference to a specific object
in the computers memory. Reassigning a variable simply switches the reference
to a different object in memory.
If the object a variable refers to in memory is altered in some way, the value
of the var corresponding to the altered object will also change.
If you perform some ops that appears to alter an immutable object, it is 
actually creating a total new object in memory, rather than changing the original
immutable object.
'''

x = "Hello"
y = x
y = y.lower()
print(x, y)

'''
List are mutable data structure that can hold multiple objects. If we alter a
list, Python does not make entirely a new list in memory; it changes the actual 
list  object itself. 
In the example below x and y still both refer to the original list, so both 
x and y have the same value, even though it may appear that the code only added 
the number 4 in the list y.
'''
x = [1, 2, 3]
y = x
y.append(4)
print(x, y)
