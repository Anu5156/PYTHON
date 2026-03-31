#WHAT IS THE DIFFERENCE BETWEEN TYPE CASTING AND TYPE CONVERSION?
#Type casting is the process of converting a value from one data type to another data type. It is done explicitly by the programmer using built-in functions like int(), float(), str(), etc. For example, if you have a string "123" and you want to convert it to an integer, you can use int("123") to get the integer value 123.
#Type conversion, on the other hand, is the process of converting a value from one data type to another data type automatically by the programming language. It is done implicitly by the interpreter when it encounters an operation that requires a certain data type. For example, if you have an integer 5 and a float 3.14, and you add them together, the interpreter will automatically convert the integer 5 to a float 5.0 before performing the addition, resulting in 8.14.
#In summary, type casting is an explicit conversion done by the programmer, while type conversion is an implicit conversion done by the programming language.

#EXAMPLE OF TYPE CASTING
#Converting a string to an integer
str_num = "123"
int_num = int(str_num)
print(int_num)  # Output: 123
print(type(int_num))  # Output: <class 'int'>


#EXAMPLE OF TYPE CONVERSION
#Adding an integer and a float
int_num = 5
float_num = 3.14
result = int_num + float_num
print(result)  # Output: 8.14
print(type(result))  # Output: <class 'float'>

#python always convert smaller data type to larger data type when performing operations between different data types. In the above example, the integer 5 is converted to a float 5.0 before the addition is performed, resulting in a float output.

int(3+4)
#output:type error: unsupported operand type(s) for +: 'int' and 'int'
#In the above example, we are trying to add two integers (3 and 4) and then convert the result to an integer using the int() function. However, since the result of the addition is already an integer (7), there is no need for type conversion, and the int() function is not necessary. The correct way to write this would be simply:
result = 3 + 4
print(result)  # Output: 7

#BOOL FUNCTION IN PYTHON
a=bool(1) #true
b=bool(0) #false
c=bool(-1) #true
d=bool("Python") #true
e=bool("") #false
#now what all can be the false values in python?
#In Python, the following values are considered false:
#1. None
#2. False
#3. 0 (zero of any numeric type, including 0.0, 0j, etc.)
#4. Empty sequences and collections (e.g., '', [], (), {}, set())
#5. Objects of user-defined classes that implement a __bool__() or __len__() method that returns False or 0, respectively.

#STRING str() function in python
f=str(123) #converts integer to string
g=str(3.14) #converts float to string
h=str(True) #converts boolean to string
i=str(None) #converts None to string
j=str(False) #converts boolean to string

