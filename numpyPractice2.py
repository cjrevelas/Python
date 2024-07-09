import numpy as np

x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x.size)
print()

# Array slicing (var[lower:upper:step])
# caution: upper bound is never included
print("----- ARRAY SLICING -----")
x = np.array([10,11,12,13,14])

print(x[1:3])
print()
print(x[1:-2]) # negative indexing works fine as well
print()

# fetch the first three elements
print(x[:3])
print()

# fetch the last two elements
print(x[-2:])
print()

# fetch every other element from beginning to end of array
print(x[::2])

# Array slicing in 2d array / matrices
print("----- ARRAY SLICING IN 2D ARRAYS -----")
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
print(x[0,3:5])
print()
print(x[4:,4:])
print()
print(x[:,2])
print()
print(x[2::2,::2])
print()

x = np.arange(25).reshape(5,5)
print(x)
print()
print(x[4,:])
print(x[-1,:])
print(x[4])
print()
print(x[:,1::2])
print(x[:,1:-1:2])
print()
print(x[1::2,:-2:2])
print(x[1::2,:-1:2])
print(x[1::2,:3:2])
print()

# We always need to have in mind how memory referening works under the hood.
# Slices are actually references to locations in memory, thus we can also
# use it in assignment operations as well.
a = np.array([1,2,3,4])

b = a[::] # = a

b[0] = -1

print(b)
print()
print(a)
print()

# This happens because b is indeed a new array, but it references the same data in memory. So when we change b, we also change
# a since the point to the same data. This may look bad, but it is actually better in terms of time and memory complexity,
# because it avoids unnecessary copies of (big) data. So b can just be considered as a different view of the original data of a.
# If we indeed wish to copy the data into a new array, we can use the .copy() method:
c = a.copy()
print(c)
c[0] = 1
print()
print(c)
print()
print(a)
