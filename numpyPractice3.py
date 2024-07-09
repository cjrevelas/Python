# Slicing: we fetch and/or modify the data of a numpy array based
# on the selection of a list of consecutive number of elements.

# Fancy indexing: we fetch and/or modify the data of a numpy array
# based directly on their indeces. The selection/indexing of elements
# can be completely random.

# Masking: we fetch and/or modify the entries of a numpy array based
# their values.

# Caution: unlike slicing, fancy indexing and masking are not views of
# the original array, which means that they do create a copy of them.

import numpy as np

# fancy indexing
x = np.arange(0,80,10)
print(x)
print()

indices = np.array([1,2,-3])
y = x[indices]
print(y)
print()

x[indices] = 100
print(x)
print()

# masking with a boolean value created by hand
mask = np.array([0,1,1,0,0,1,0,0], dtype = bool)
y = x[mask]
print(y)
print()

# a more realistic example of masking
x = np.array([-20,-5,2,10,-8,9,18])
mask_negative = x < 0
print(mask_negative)
print()
print(type(mask_negative))
print()
print(x[mask_negative])
print()

r1 = np.arange(0,6)
r2 = np.arange(10,16)
r3 = np.arange(20,26)
r4 = np.arange(30,36)
r5 = np.arange(40,46)
r6 = np.arange(50,56)

x = np.array([r1])
x = np.append(x, [r2], axis = 0)
x = np.append(x, [r3], axis = 0)
x = np.append(x, [r4], axis = 0)
x = np.append(x, [r5], axis = 0)
x = np.append(x, [r6], axis = 0)

print(x)
print()

print(x[[0,1,2,3,4],[1,2,3,4,5]]) # fancy indexing in both the rows and the columns
print()
print(x[3:,[0,2,5]]) # slicing in the rows and fancy indexing in the columns
print()
mask = np.array([1,0,1,0,0,1], dtype = bool)
print(x[mask,2::2]) # masking in the rows and slicing in the columns
print()

# Another simple example of fancy indexing
x = np.arange(25).reshape(5,5)
print(x)
print()

print(x[[0,2,3,3],[2,3,1,-1]])
print()

# Another example of masking: select the number in x that are divisible by 3
divisible = x % 3 == 0
print(x[divisible])
print()
print(x % 3)
print()
