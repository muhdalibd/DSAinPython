'''
    🟧  What is NumPy?
    NumPy is a Python library used for working with arrays.
    It also has functions for working in domain of linear algebra, fourier transform, and matrices.
    NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
    NumPy stands for Numerical Python.

    🟧  Why Use NumPy?
    In Python we have lists that serve the purpose of arrays, but they are slow to process.
    NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
    The array object in NumPy is called ndarray, it provides a lot of supporting
        functions that make working with ndarray very easy.
    Arrays are very frequently used in data science, where speed and resources are very important.

    🟧  Why is NumPy Faster Than Lists?
    NumPy arrays are stored at one continuous place in memory unlike lists, so
        processes can access and manipulate them very efficiently.
    This behavior is called locality of reference in computer science.
    This is the main reason why NumPy is faster than lists. Also it is optimized
        to work with latest CPU architectures.

    🟧  Which Language is NumPy written in?
    NumPy is a Python library and is written partially in Python, but most of the
        parts that require fast computation are written in C or C++.
'''



import numpy as np  #   NumPy is usually imported under the np alias.
# alias: In Python alias are an alternate name for referring to the same thing.

'''
    🟧  Checking NumPy Version
'''
# print(np.__version__)

'''
    🟧  NumPy Creating Arrays
    NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    We can create a NumPy ndarray object by using the array() function.
    To create an ndarray, we can pass a list, tuple or any array-like object
        into the array() method, and it will be converted into an ndarray:
'''

arr = np.array([1,2,3,4,5]) #   list
# print(arr)
# print(type(arr))    #   type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

arr = np.array((1,2,3,4,5,6))   #   tuple
# print(arr)
# print(type(arr))


'''
    🟧  Dimensions in Arrays
    Check Number of Dimensions?
        NumPy Arrays provides the ndim attribute that returns an integer
        that tells us how many dimensions the array have.
'''
arr = np.array(42)  #   0-D Array
# print(arr)
# print(arr.ndim)

arr = np.array([1,2,3,4,5]) #   1-D Array
# print(arr)
# print(arr.ndim)

arr = np.array([    #   2-D Array
    [1,2,3],
    [3,4,5]
])
# print(arr)
# print(arr.ndim)

arr = np.array([    #   3-D Array
    [[1,2,3], [3,4,5]],
    [[4,5,6], [6,7,8]]
])
# print(arr)
# print(arr.ndim)


'''
    🟧  Higher Dimensional Arrays
    An array can have any number of dimensions.
    When the array is created, you can define the number of dimensions by using the ndmin argument.
'''

arr = np.array([1,2,3,4,5], ndmin=5)
# print(arr)
# print(arr.ndim)


'''
    🟧  NumPy Array Indexing
    Array indexing is the same as accessing an array element.
'''

arr = np.array([1,2,3,4,5])
# print(arr[2])
# print(arr[2] + arr[3])

arr = np.array([
    [1,2,3,4,5],
    [5,6,7,8,9]
])
# print(arr[1,2])
# print(arr[1][2])

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
# print(arr.ndim)
# print(arr[0,1,2])
# print(arr[0][1][2])

'''
    Example Explained:
    arr[0, 1, 2] prints the value 6.
    👉  And this is why:

    The first number represents the first dimension, which contains two arrays:
    [[1, 2, 3], [4, 5, 6]]
    and:
    [[7, 8, 9], [10, 11, 12]]
    Since we selected 0, we are left with the first array:
    [[1, 2, 3], [4, 5, 6]]
    The second number represents the second dimension, which also contains two arrays:
    [1, 2, 3]
    and:
    [4, 5, 6]
    Since we selected 1, we are left with the second array: [4, 5, 6]
    The third number represents the third dimension, which contains three values:  4 5 6
    Since we selected 2, we end up with the third value: 6
'''


'''
    🟧  Negative Indexing
    Use negative indexing to access an array from the end.
    Indexing start from -1. [Normally start from 0]
'''

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
# print(arr[-2,-1,-1])