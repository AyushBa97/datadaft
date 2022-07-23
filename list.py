"""
LIST ARE MUTABLE, HETEROGENEOUS, ORDERED COLLECTION OF OBJECTS.
"""

my_list = ["Lesson", 5, "Is Fun?", True]
print(my_list)

second_list = list("Life is Study".split())
print(second_list)

empty_list = []
print(empty_list)

empty_list.append("List is no longer empty")
print(empty_list)

my_list.remove(5)
print(my_list)

combine_list = my_list + empty_list
print(combine_list)

combine_list.extend(second_list)
print(combine_list)

num_list = [1, 3, 5, 7, 9]
print(len(num_list), 'len')
print(max(num_list), 'max')
print(min(num_list), 'min')
print(sum(num_list), 'sum')
print(sum(num_list) / len(num_list), 'mean')

print(1 in num_list)
print(1 not in num_list)

print(num_list.count(3))

num_list.reverse()
print(num_list)

num_list.sort()
print(num_list)

print(combine_list[0])
print(combine_list[2])
print(combine_list[-1])
print(combine_list[-3])

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][2])

slice_list = combine_list[1:4]  # slice index 1,2 & 3
print(slice_list)

slice_list = combine_list[1:6:2]
print(slice_list)

slice_list2 = combine_list[1:]
slice_list3 = combine_list[:6]
slice_list4 = combine_list[6:2:-1]

print(slice_list2)
print(slice_list3)
print(slice_list4)

rev_list = combine_list[::-1]
print(rev_list)

num_list[3] = "new"
print(num_list)
del num_list[3]
print(num_list)

# list_name.pop() # pop() removes element from the end of the list

list1 = [1, 2, 3]
list2 = list1.copy()
list1.append(4)
print(list1)
print(list2)

import copy

list2 = ["lies within list", list1]
list3 = copy.deepcopy(list2)
print(list2)
print(list3)
list3.append(4)
print(list2)
print(list3)
