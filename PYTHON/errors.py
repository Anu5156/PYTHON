#types of errors
# 1. Syntax Error
# 2. Runtime Error
# 3. Logical Error

#1. Syntax Error
# print("hello world"
#output: SyntaxError: unexpected EOF while parsing, because there is a missing closing parenthesis at the end of the print statement.
"""ON\errors.py", line 7
    print("hello world"
         ^
SyntaxError: '(' was never closed"""

#2. Runtime Error/exception
print(10/0)
""" print(10/0)
          ~~^~
ZeroDivisionError: division by zero"""

#3. Logical Error
a=10
b=20
if a>b:
    print("a is greater than b")
#output: (no output), because the condition a>b is false, so the print statement inside the if block is not executed. This is a logical error because the code runs without any syntax or runtime errors, but it does not produce the expected output.

#keyword error
def my_function():
    pass
my_function()
#output: (no output), because the function my_function is defined but not called. This is a keyword error because the function is not being used correctly, but it does not produce any syntax or runtime errors.


