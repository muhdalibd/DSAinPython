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

#   Python List
# my_list = [1,2,3,4,5]
# print(my_list)
# my_list = my_list * 2
# print(my_list)


import numpy as np  #   NumPy is usually imported under the np alias.
# alias: In Python alias are an alternate name for referring to the same thing.

#   Numpy Arrays
# arr = np.array([1,2,3,4,5])
# arr = arr * 2
# print(arr)

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



'''
    🟧  Slicing arrays
    Slicing in python means taking elements from one given index to another given index.
    We pass slice instead of index like this:   [start:end].
    We can also define the step, like this:     [start:end:step].
    If we don't pass start its considered 0
    If we don't pass end its considered length of array in that dimension
    If we don't pass step its considered 1
'''

arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5])
# print(arr[4: ])
# print(arr[:4 ])
# print(arr[1:5:3])
# print(arr[ : :2])

'''
    🟧  Slicing 2-D Arrays
'''
arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
# print(arr[1,1:4])
# print(arr[0:2,2])

'''
    🟧  Negative Slicing
'''

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# print(arr[-3:-1, 2])    #   [start : stop] =>   stop > start


'''
    🟧  NumPy Data Types
    👉  Data Types in Python
    By default Python have these data types:

    strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
    integer - used to represent integer numbers. e.g. -1, -2, -3
    float - used to represent real numbers. e.g. 1.2, 42.42
    boolean - used to represent True or False.
    complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

    👉  Data Types in NumPy
    NumPy has some extra data types, and refer to data types with one character,
        like i for integers, u for unsigned integers etc.
    Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
'''

'''
    🟧  Checking the Data Type of an Array
    The NumPy array object has a property called dtype that returns the data type of the array:
'''

arr = np.array([1,2,3,4,5])
# print(arr.dtype)
arr = np.array(["apple", "banana", "chery"])
# print(arr.dtype)

'''
    Creating Arrays With a Defined Data Type
'''
arr = np.array([1,2,3,4,5], dtype='S')  #   i, u, f, S and U
# print(arr)
# print(arr.dtype)
# arr = np.array(['a', '2', '3'], dtype='i')  #   ValueError

'''
    Converting Data Type on Existing Arrays
    The best way to change the data type of an existing array, is to make a copy
    of the array with the astype() method.
    The astype() function creates a copy of the array, and allows you to specify
    the data type as a parameter.
'''
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)    #   int64
newarr = arr.astype('i')    #   int32
newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)


'''
    🟧  NumPy Array Copy vs View
    The Difference Between Copy and View
    The main difference between a copy and a view of an array is that
        the copy is a new array, and the view is just a view of the original array.
    The copy owns the data and any changes made to the copy will not affect
        original array, and any changes made to the original array will not affect the copy.
    The view does not own the data and any changes made to the view will affect
        the original array, and any changes made to the original array will affect the view.
'''
#   COPY
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
# print(arr)
# print(x)

#   VIEW
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] =42
x[2] = 31
# print(arr)
# print(x)

'''
    Check if Array Owns its Data
    As mentioned above, copies owns the data, and views does not own the data,
        but how can we check this?
    Every NumPy array has the attribute base that returns None if the array owns the data.
    Otherwise, the base  attribute refers to the original object.
'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
# print(x.base)
# print(y.base)


'''

'''