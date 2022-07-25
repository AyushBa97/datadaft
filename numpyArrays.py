"""
Numpy implements the n-dimensional array or the ndarray similar to lists in that
they contain a collection of items that can be accessed via indexes.
On the other hand , ndarrays are homogeneous, meaning they can only contain obejcts
if the same type, and they can be multidimensional.

Use for mathematical ops and adv linear ops
"""

# importing numpy package
import numpy as np

my_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]

my_array = np.array(my_list)
two_d_array = np.array([my_list, second_list])
print(two_d_array, type(two_d_array))
print(two_d_array.shape)
print(two_d_array.size)
print(two_d_array.dtype)

# creating identity matrix
identity_matrix = np.identity(n=4)  # n is size of the array
print(identity_matrix)

# create an array filled with ones
print(np.ones(shape=[2, 5]))

# create an array filled with zeros
print(np.zeros(shape=[2, 5]))

# indexing and slicing numpy 1-D arrays
# my_array = [1, 2, 3, 4]

print(my_array[3])
print(my_array[2:])
print(my_array[::-1])

# indexing and slicing numpy 2-D arrays
'''
two_d_array = [[1, 2, 3, 4]
               [5, 6, 7, 8]]
'''

two_d_array = np.array([my_array, my_array + 6, my_array + 12])
print(two_d_array)
print(two_d_array[1, 3])  # indexing
print(two_d_array[1:, 2:])  # slicing
print(two_d_array[::-1, ::-1])  # reverse

# reshaping arrays
ar = np.reshape(a=my_array,
                newshape=(2, 2))
print(ar)

# Unravel a multidimensional array into 1-D array
ar2 = np.ravel(a=two_d_array,
               order='C')  # unravel  by rows
print(ar2)

ar3 = np.ravel(a=two_d_array,
               order='F')  # unravel  by columns
print(ar3)

ar4 = two_d_array.flatten()
print(ar4)

# Transpose
print(two_d_array.T)

# flip horizontally vertically
print(np.flipud(two_d_array))

# flip left right
print(np.fliplr(two_d_array))

# rotate an array counter-clockwise 90 degrees where k is number of 90 deg rotation
print(np.rot90(two_d_array, k=1))

# shift elements in an array, shift elements 2 positions in each row in the below example
print(np.roll(a=two_d_array,
              shift=2,
              axis=1))

# concatenate two numpy arrays

ar_join = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
ar_1 = np.concatenate((two_d_array, ar_join), axis=1)  # array to join, axis to join upon
print(ar_1)

# arithmetic ops to every element
print(two_d_array + 100)
print(two_d_array * 100)
print(two_d_array // 100)
print(two_d_array ** 100)

print(np.mean(two_d_array))
print(np.mean(two_d_array, axis=1))  # mean of each column
print(np.std(two_d_array))
print(np.std(two_d_array, axis=1))  # standard deviation of each column
print(np.sum(two_d_array, axis=1))  # get the row sums
print(np.sum(two_d_array, axis=0))  # get the column sums

print(np.log(two_d_array))  # log of all elements in array
print(np.sqrt(two_d_array))  # sqrt of all elements in array

# dot product
print(np.dot(two_d_array[0, 0:], two_d_array[1, 0:]))  # Slice row 0 , Slice row 1

# matrix multiplication
print(np.dot(two_d_array[2:][2:], two_d_array[:2][:2]))
