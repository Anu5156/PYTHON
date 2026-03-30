"""
| Type  | Example |
| ----- | ------- |
| int   | 10      |
| float | 3.14    |
| str   | "hello" |
| bool  | True    |
| list  | [1, 2, 3] |
| tuple | (1, 2, 3) |
| dict  | {"key": "value"} |
| set   | {1, 2, 3} |
| NoneType | None |

"""
#example
x = 10 #integer value
print(x)
y = 3.5 #float value
print(y)
name = "Anushka" #string value
print(name)
is_ok = True #boolean value
print(is_ok)
my_list = [1, 2, 3] #list value
print(my_list)
my_tuple = (1, 2, 3) #tuple value
print(my_tuple)
my_dict = {"key": "value"} #dictionary value
print(my_dict)
my_set = {1, 2, 3} #set value
print(my_set)
my_none = None #None value
print(my_none)


"""🧠 EXPLANATION (IMPORTANT)
Python has several built-in data types:
- int: integer values
- float: floating-point values
- str: string values
- bool: boolean values
- list: ordered, mutable collections
- tuple: ordered, immutable collections
- dict: unordered collections of key-value pairs
- set: unordered collections of unique elements
- NoneType: a special type representing the absence of a value

Each variable in Python has a type, which is determined at runtime.

what is mutable?
Mutable means that the value of the variable can be changed after it is created. For example, lists and dictionaries are mutable because you can add, remove, or change their elements. On the other hand, strings and tuples are immutable because once they are created, their values cannot be changed."""
 
"""🧠 CHECK TYPE"""
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_ok))  # Output: <class 'bool'>
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_dict))  # Output: <class 'dict'>
print(type(my_set))  # Output: <class 'set'>
print(type(my_none))  # Output: <class 'NoneType'>

print(type("10"))  # Output: <class 'str'>, because "10" is a string, not an integer.

#🔥 TRICKY QUESTION 3
x = True
print(x + 1)
# Output: 2, because in Python, True is treated as 1 and False is treated as 0 when used in arithmetic operations. So, True + 1 is equivalent to 1 + 1, which equals 2.

a = [1, 2, 3]
b = a
b.append(4)
print(a)

def add(x):
    return x + x

print(add(5))      # works
print(add("Hi"))   # works

def greet(name):
    return "Hello,"+name
print(greet("Anushka"))
