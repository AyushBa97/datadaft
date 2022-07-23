"""
DICTIONARY STORES COLLECTION OF VALUE IN KEY VALUE PAIR
THEY ARE MUTABLE
DICTIONARIES KEY MUST BE AN IMMUTABLE OBJECT
VALUES CAN BE ANYTHING, HETEROGENEOUS IN NATURE
"""
import pprint

my_dict = {
    'name': 'Joe',
    'age': 10,
    'city': 'Germany'
}

print(my_dict)
print(my_dict["name"])
print(len(my_dict))

# checks only the keys for dictionary
print('name' in my_dict)
print('Joe' in my_dict)

my_dict["new_key"] = "new_value"
print(my_dict)

del my_dict["new_key"]
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_table = {
    "name": ["Joe", "Bob", "Harry"],
    "age": [10, 15, 20],
    "city": ["Paris", "New York", "Tokyo"]
}

pprint.pprint(my_table)

"""
SET ARE UNORDERED, MUTABLE COLLECTION OF IMMUTABLE OBJECTS
THAT CANNOT CONTAIN DUPLICATED.
SETS DO NOT SUPPORT INDEXING LIKE LIST [eg: l[2]]
"""

my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)
print(type(my_set))

my_set.add(8)
print(my_set)

my_set.remove(7)
print(my_set)

print(len(my_set))
print(max(my_set))
print(min(my_set))
print(sum(my_set))

print(5 in my_set)

set1 = {1, 3, 5, 6}
set2 = {1, 2, 3, 4}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print({2, 3}.issubset(set2))
print({1, 2}.issubset(set1))

my_list = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7]
print(set(my_list))

print(list(set(my_list)))
