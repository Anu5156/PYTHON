#for loop:
"""it allows us to run a block of code multiple time
FOR LOOP is present in lots of programming language,though syntax and behaviour can be different"""

"""
syntax:
for some_var in some_collection:
    <statement1>
    <statement2>
    <statement3>"""
for i in 'python':
    print(i)
"""output:
p
y
t
h
o
n
"""
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit[0])#
# a
# b
# c

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruits[0])
"""apple
apple
apple"""