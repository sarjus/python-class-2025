import numpy as np
array1 = np.random.randint(0,20,(3,3))
array2 = np.random.randint(0,20,(3,3))
array3 = array1+array2
print("First Array")
print(array1)
print("Second Array")
print(array2)
print("Addition")
print(array3)
print("Mean")
print(np.mean(array1))
print("Standard Deviation")
print(np.std(array1))
#Multiply each element of first matrix by a scalar value
scalar = 3
array4 = array1 * scalar
print("Multiplication")
print(array4)
#dot product of the matrix
array5 = np.dot(array1, array2)
print("Dot product")
print(array5)