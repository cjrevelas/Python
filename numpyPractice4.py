# Calculations between numpy arrays

# Rules
# 1. Operations among multiple array objects are first checked for proper shape match.

# 2. Mathematical operators apply element-by-element on the values.

# 3. Reduction operations (mean, std, max, min) apply to the whole array, unless
#    a certain axis is specified.

# 4. Missing values propagate unless explicitly ignored.

import numpy as np

x = np.arange(1,7).reshape(2,3)
print(x)
print()

print(x.sum())
print()
print(x.sum(axis=0))
print()
print(x.sum(axis=1))
print()

# Retrive positions of maximum values
x = np.array([2,4,5,5])

mask = x == x.max()

print(mask)
print()

print(np.where(mask))
