"""
TUPLES ARE IMMUTABLE SEQUENCE DATA TYPE USED FOR SHORT
COLLECTION OF RELATED DATA . CAN STORE HETEROGENEOUS DATA.
"""

tup = (1, 2, 3)
print(tup)

l = [2, 3, 1, 4]
tup2 = tuple(l)
print(tup2)

print(tup2[2:4])
print(max(tup2))
print(min(tup2))
print(len(tup2))
print(sum(tup2))

multiline_string = '''STRINGS ARE 
IMMUTABLE SEQUENCE 
OF TEXT CHARACTER
'''

string = "Hello World"
print(string[3])
print(string[3:])
print(string[:2])
print(len(string))
print(string.count("l"))
print(string.lower())
print(string.upper())
print(string.title())
print(string.find('r'))
print(string.replace('World', 'Friend'))
print(string.split())
print(string.split('o'))

print(multiline_string.splitlines())

print("  strip func   ".strip())
print("  strip func   ".lstrip())
print("  strip func   ".rstrip())

print("Hello" + " World")
print(" ".join(["Hello", "world", "Join", "Me!"]))
print('a'+str(1))

place = 'Kolkata'
name = "Bandoji"
print(f'{name} is from {place} ')


