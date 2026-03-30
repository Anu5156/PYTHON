a=10
A="python"
print(a) #output: 10, because the variable a is assigned the value 10 and is printed using the print function.
print(type(a))#output: <class 'int'>, because the variable a is of type integer (int) in Python.
print(A) #output: python, because the variable A is assigned the value "python" and is printed using the print function.
print(type(A))#output: <class 'str'>, because the variable A is of type string (str) in Python.

b=3.14
print(b) #output: 3.14, because the variable b is assigned the value 3.14 and is printed using the print function.
print(type(b))#output: <class 'float'>, because the variable b is of type float in Python.

"""types of data in Python are:
TEXT TYPE: str
NUMERIC TYPES: int, float, complex
SEQUENCE TYPES: list, tuple, range
MAPPING TYPE: dict
SET TYPES: set, frozenset
BOOLEAN TYPE: bool
NONE TYPE: NoneType
Binary Types: bytes, bytearray, memoryview

"""
#datatypes in Python are dynamic, which means that you don't need to declare the type of a variable when you create it. The type of a variable is determined at runtime based on the value assigned to it. You can also change the type of a variable by assigning a different value to it.
#datatypes are unbounded, which means that they can grow or shrink in size as needed. For example, a list can contain any number of elements, and a string can be of any length.
#size of the datatypes are also dynamically managed by Python, which means that you don't need to worry about the memory allocation for different datatypes. Python automatically manages the memory for you based on the size of the data being stored.

#TEXT TYPE: str
c = "Hello, World!"
print(c) #output: Hello
print(type(c))#output: <class 'str'>, because the variable c is of type string (str) in Python.


#NUMERIC TYPE:int,float,complex
d = 42
print(type(a))#output: <class 'int'>, because the variable d is of type integer (int) in Python.

e = 3.14
print(type(e))#output: <class 'float'>, because the variable e is of type float in Python.

f = 2 + 3j
print(type(f))#output: <class 'complex'>, because the variable f is of type complex in Python, which represents a complex number with a real part (2) and an imaginary part (3j).

#SEQUENCE TYPE: list, tuple, range

g = [1, 2, 3, 4, 5]
print(type(g))#output: <class 'list'>, because the variable g is of type list in Python, which is a mutable sequence type that can contain elements of different types.

h = (1, 2, 3, 4, 5)
print(type(h))#output: <class 'tuple'>, because the variable h is of type tuple in Python, which is an immutable sequence type that can contain elements of different types.

i = range(1, 10)
print(type(i))#output: <class 'range'>, because the variable i is of type range in Python, which represents a sequence of numbers and is commonly used for looping a specific number of times in for loops.

#MAPPING TYPE: dict
j = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in j.items():
    print(key, ":", value)
#output: name : Alice
#output: age : 30
#output: city : New York

#set types: set, frozenset
k = {1, 2, 3, 4, 5}
print(type(k))#output: <class 'set'>, because the variable k is of type set in Python, which is an unordered collection of unique elements.

l= frozenset({1, 2, 3, 4, 5})
print(type(l))#output: <class 'frozenset'>, because the variable l is of type frozenset in Python, which is an immutable version of a set that cannot be modified after it is created.
print(l) #output: frozenset({1, 2, 3, 4, 5}), because the variable l is a frozenset that contains the unique elements {1, 2, 3, 4, 5} and is printed using the print function.

#BOOLEAN TYPE: bool
m = True
print(type(m))#output: <class 'bool'>, because the variable m is of type bool in Python, which represents a boolean value that can be either True or False.

n= False
print(type(n))#output: <class 'bool'>, because the variable n is of type bool in Python, which represents a boolean value that can be either True or False.

#none type: NoneType

o = None
print(type(o))#output: <class 'NoneType'>, because the variable o is of type NoneType in Python, which represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything.

#BINARY TYPES: bytes, bytearray, memoryview

p = b"Hello, World!"
print(type(p))#output: <class 'bytes'>, because the variable p is of type bytes in Python, which represents a sequence of bytes and is commonly used for binary data such as images or files.

q = bytearray(b"Hello, World!")
print(type(q))#output: <class 'bytearray'>, because the variable q is of type bytearray in Python, which is a mutable sequence of bytes that can be modified after it is created.

r = memoryview(b"Hello, World!")
print(type(r))#output: <class 'memoryview'>, because the variable r is of type memoryview in Python, which is a view object that allows you to access the memory of a bytes-like object without copying it. It is often used for efficient manipulation of large binary data.


#TO GET SIZE OF THE DATATYPE
from numpy import size 

import sys
c=1000
print(size(c))#output: 1, because the size of the integer 1000 in Python is 1 bytes. The size of an integer can vary depending on the value and the platform, but in this case, it is 28 bytes.
print(sys.getsizeof(c))#output: 28, because the getsizeof function from the sys module returns the size of the object in bytes, which is 28 bytes for the integer 1000 in Python.

c=10000000000000000000000000000000000000000000000000000000000000
print(sys.getsizeof(c))
#output: 32, because the size of the integer 100
