#in python string(str) is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are used to represent text data in Python. They can contain letters, numbers, symbols, and whitespace characters.

"""Python does not have a char data type,unlike c,c++ or java.  """

"""Single('') or double (" ") quotes can be used to create a string in Python. Both are functionally equivalent, and you can choose either based on your preference or to avoid the need for escaping characters."""

a="Mayank"
print(a)
#output:Mayank

b="Priyanka"
print(b)
#output:Priyanka

single_quote_string = 'Hello, World!'
print(single_quote_string)
#output: Hello, World!

double_quote_string = "Hello, World!"
print(double_quote_string)
#output: Hello, World!

multi_line_string = '''This is a multi-line string.
It can span multiple lines.'''
print(multi_line_string)
#output: This is a multi-line string.
#         It can span multiple lines.


# "\n"#new line character
# "\t"#tab character
# "\\"#backslash character
# "\'"#single quote character
"""Python uses UNICODE number system inlike C which uses ASCII"""
"""UNICODE is a number system which supports much wider range of character compared to ASCII .It also supports multiple languages"""

#ex1:
unicode_string = "Hello, 你好!"
print(unicode_string)
#output: Hello, 你好!

#ex2:
unicode_string = "Python is great! 🐍"
print(unicode_string)
#output: Python is great! 🐍

