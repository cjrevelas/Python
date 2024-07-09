import numpy as np
import time
import sys

'''
The main object of Numpy (Numerical Python) is a multidimensional array.

This array contains elements of the same type indexed by a tuple of positive integers.

In the context of Numpy, we refer to array dimensions as "axes".
'''

def main() -> None:
    # Basic numpy array initialization syntax
    print("----- Basic numpy initilization syntax -----")
    a = np.array([1,2,3])
    print(a)
    print()

    # Characteristics of a numpy array
    print("----- Characteristics of a numpy array -----")
    x1 = np.array([1,2,3,4,5])
    print(x1, '\n')
    print("Number of dimensions/axes: ", x1.ndim, '\n')
    print("Shape (number of elements along each axis): ", x1.shape, '\nA')
    print("Type of elements: ", x1.dtype,'\n')

    y1 = np.arange(1,6,1, dtype = np.double)
    print(y1, '\n')
    print("Number of dimensions/axes: ", y1.ndim, '\n')
    print("Shape (number of elements along each axis): ", y1.shape, '\n')
    print("Type of elements: ", y1.dtype, '\n')

    x2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    print(x2, '\n')
    print("Number of dimensions/axes: ", x2.ndim, '\n')
    print("Shape (number of elements along each axis): ", x2.shape, '\n')
    print("Type of elements: ", x2.dtype, '\n')

    y2 = np.arange(1,11,1).reshape((2,5))
    print(y2, '\n')
    print("Number of dimensions/axes: ", y2.ndim, '\n')
    print("Shape (number of elements along each dimension/axis): ", y2.shape, '\n')
    print("Type of elements: ", y2.dtype, '\n')

    # Comparing a numpy array to a python list
    print("----- Comparing a numpy array to a python list -----")
    b = range(1000)
    print(sys.getsizeof(5) * len(b))
    print()

    c = np.arange(1000)
    print(c.itemsize * c.size)
    print()

    size = 100000

    l1  = range(size)
    l2  = range(size)
    rs1 = [None] * size

    n1 = np.arange(size)
    n2 = np.arange(size)

    startTime = time.time()

    for ii in range(size):
        rs1[ii] = l1[ii] + l2[ii]

    endTime = time.time()

    print("python list addition time (ms): ", (endTime - startTime) * 1000)
    print()

    startTime = time.time()

    rs2 = n1 + n2

    endTime = time.time()

    print("numpy array addition time (ms): ", (endTime - startTime) * 1000)
    print()

    # Let's work with our first 2d array
    print("----- Working with multidimensional arrays -----")

    a = np.array([ [1,2,3], [4,5,6] ])
    print(a)
    print()

    print(a[:,0])
    print(a[:,1])
    print(a[:,2])
    print()

    print(a[0,:])
    print(a[1,:])
    print()

    print("----- Flattening a multi-dimensional array -----")
    b1 = a.flatten()
    print(b1)
    b2 = a.reshape((6,))
    print(b2)
    b3 = a.reshape((1,6))
    print(b3)
    b4 = a.reshape((6,1))
    print(b4)
    print()

    c = np.append(b3, [[11, 12, 13, 14, 15, 16]], axis = 0)
    print(c)
    print()

    c = np.append(b4, [[11], [12], [13], [14], [15], [16]], axis = 1)
    print(c)
    print()

    a = np.array([[4,7], [2,8], [5, 6]])
    print(a)
    print(a.ndim) # number of axes/dimensions
    print(a.itemsize)
    print(a.shape) # number of elements along each axis/dimension
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float32)
    print(a.itemsize)
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float64)
    print(a)
    print(a.itemsize)
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=complex)
    print(a)
    print(a.itemsize)
    print()

    # Initialization of a numpy array of a certain shape
    print("----- Initializaing numpy arrays with a certain shape -----")
    a = np.zeros((3,4))
    print(a)
    print()

    a = np.zeros((3,4), dtype = int)
    print(a)
    print()

    a = np.ones((3,4))
    print(a)
    print()

    a = np.arange(10)
    print(a)
    print()

    # Reshaping an array
    print("----- Reshaping arrays -----")
    a = np.arange(9)
    print(a)

    b = a.reshape(3,3)
    print(b)
    print()

    c = b.flatten()
    print(c)

    c = b.flatten(order='F')
    print(c)
    print()

    d = np.arange(20).reshape(4,5)
    print(d)
    print()

    k = np.transpose(d)
    print(k)
    print()

    a = np.arange(8).reshape(2,4)
    print(a)
    print()

    b = a.reshape(2,2,2)
    print(b)
    print()

    x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    print(x)
    print()

    print(np.swapaxes(x,0,2))
    print()

    # Arithmetic operations on numpy arrays
    print("----- Performing arithmetic operations on numpy arrays -----")
    a = np.arange(9).reshape(3,3)
    print(a)
    print()

    b = a + 10
    print(b)
    print()

    b = a * 10
    print(b)
    print()

    c = np.add(a,np.array([10,10,10]))
    print(c)
    print()

    c = a + np.array([10,10,10])
    print(c)
    print()

    c = a + np.array([10,100,1000])
    print(c)
    print()

    # Merging and splitting arrays
    print("----- Merging and splitting arrays -----")
    a1 = [[1,2,3,4,5,6],
          [7,8,9,10,11,12]]
    print(a1)
    print()

    a2 = [[11,12,13,14,15,16],
          [17,18,19,20,21,22]]
    print(a2)
    print()

    a3 = np.concatenate((a1, a2), axis=0)
    print(a3)
    print()

    a4 = np.concatenate((a1, a2), axis=1)
    print(a4)
    print()

    a5 = np.vstack((a1,a2))
    print(a5)
    print()

    a6 = np.hstack((a1,a2))
    print(a6)
    print()

    a7 = np.stack((a1,a2))
    print(a7)
    print()

    print(a7.shape)
    print()

if __name__ == "__main__":
    main()
