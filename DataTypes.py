print(type(2))
print(type(2.12))
print(type(1 / 2))
print(type(1.0))
print(isinstance(1.0, float), 'using isinstance')
print(type(int(1.0)), 'int typecasting')  # typecasting
print(type(float(1)), 'float typecasting')

'''
Float can take on few special values:
Inf  : Infinity
-Inf : Negative Infinity
NaN  : not a number , it's sometimes used as a placeholder for missing or erroneous numerical values.
'''
print(type(float("Inf")), 'inf')
print(type(float("-Inf")), '-inf')
print(type(float("NaN")), 'Nan')

# Python also contains an uncommon numerical data type "complex" which is used to store complex number.

print(type(True))
print(type(False))
print(type(isinstance(False, bool)))
print(type(isinstance(True, bool)))
print(20 > 10)
print(20 < 10)
print(20 >= 10)
print(20 <= 20)
print(16 == 16)
print(16 == 16.00)  # equivalent int and float are considered equal
print(20 != 10)
print((20 > 10) and (9 > 5))
print((20 > 10) or (9 > 5))

'''
Execution Order in Logical Statement Operation

comparison such as >,<,>=,<=,==,!= are executed first
followed by
NOT < AND < OR

'''

print(2 > 1 or 10 < 8 and not True)
print(((2 > 1) or (10 < 8)) and (not True))

print(bool(0))  # Bool - False
print(bool(1))  # Bool - True
print(bool(2))  # Any number other than 0 is true but w.r.y boolean value system 0 is/represents False and 1 is/represents True


print(type('cat'))
print(type('1'))
print(type('')) # represents empty strings

print(type(None)) # It is a special Data Type that is often used to represent missing val.


