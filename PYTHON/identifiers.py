#what are identifiers?
#identifiers are the names given to variables, functions, classes, etc. in Python. They are used to identify and refer to these entities in the code.

#rules for naming identifiers in Python:
#1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
#2. An identifier cannot start with a digit.
#3. An identifier cannot be a reserved keyword in Python (e.g., if, else, for, while, etc.).
#4.it can start with underscore but it is not recommended to start with underscore because it is used for special purposes in Python (e.g., _private_variable, __init__, etc.).
#5. An identifier is case-sensitive, which means that myVariable and myvariable are considered different identifiers in Python.

#examples of valid identifiers

# my_variable = 10
# print(my_variable)
#output: 10, because my_variable is a valid identifier that follows the rules for naming identifiers in Python.

# example for invalid identifier

# raise=1000
#output: SyntaxError: invalid syntax, because raise is a reserved keyword in Python and cannot be used as an identifier.

# as=1000
# print(as)

"""    as=1000
    ^^
SyntaxError: invalid syntax, because as is a reserved keyword in Python and cannot be used as an identifier."""


"""identifiers cant be keywords"""
"""there are 32 keywords in Python, which are reserved words that have special meaning in the language and cannot be used as identifiers. Some examples of keywords in Python include: if, else, for, while, def, class, return, import, etc. Using a keyword as an identifier will result in a syntax error."""

"""#2. An identifier cannot start with a digit."""
# 1variable = 10
# print(1variable)
""" output: SyntaxError: invalid syntax, because 1variable starts with a digit and cannot be used as an identifier."""

#but it can be start with alphabetand then followed by the numbers
# my_variable1 = 10
# print(my_variable1)
#output: 10, because my_variable1 is a valid identifier that starts with an alphabet and is followed by numbers, which is allowed in Python.

#ex:
# _my_variable = 10
# print(_my_variable)
#output: 10, because _my_variable is a valid identifier that starts with an underscore and is followed by letters, which is allowed in Python. However, it is generally not recommended to start identifiers with an underscore unless they are intended to be private variables or functions.

# _ = 10
# print(_)
#output: 10, because _ is a valid identifier that consists of a single underscore character. It is often used as a placeholder variable or to indicate that a value is being intentionally ignored in Python.


#5. An identifier is case-sensitive, which means that myVariable and myvariable are considered different identifiers in Python.
abc=20
ABC=30
print(abc)
print(ABC)
"""output:20
30, because abc and ABC are considered different identifiers in Python due to case sensitivity. The variable abc is assigned the value 20, while the variable ABC is assigned the value 30, and both values are printed separately."""

