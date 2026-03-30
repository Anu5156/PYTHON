#concatenation in python
#for string it adds the two strings together
a="Mayank"
b="Anushka"
c=a+b
print(c)
#output: MayankAnushka, because the + operator is used to concatenate the two strings 'Mayank' and 'Anushka', resulting in 'MayankAnushka'.with no space in between. If you want to add a space between the two strings, you can modify the code as follows:

#for number it acts as the arithmatic operator and adds the two numbers together
d=5
e=10
f=d+e
print(f)
#output: 15, because the + operator is used to add the two numbers 5 and 10 together, resulting in 15.

#using arithmatic operator with string and number will give us error

a=15
b="Anushka"
c=a+b
print(c)
#output: TypeError: unsupported operand type(s) for +: 'int' and 'str', because the + operator cannot be used to add an integer (int) and a string (str) together in Python. The types of the operands are incompatible for concatenation or addition, resulting in a TypeError.

#if we add two numbers as string:
a="12"
b="34"
c=a+b
print(c)
#output: 1234, because when we use the + operator with two strings '12' and '34', it concatenates them together, resulting in the string '1234'. The + operator does not perform arithmetic addition in this case, but rather string concatenation.

 #+ operator in string act as the concatenation operator, which combines two strings together without any space, while in the case of numbers, it acts as the addition operator, which sums the values.but if we want the space between the two strings we can add a space in between the two strings as follows:
a="Anushka"
b="pryianka"
c=a+" "+b
print(c)
#output: Anushka pryianka, because the + operator is used to concatenate the two strings 'Anushka' and 'pryianka' with a space in between, resulting in 'Anushka pryianka'.

#print Anushka 10 times
print("Anushka "*10)
#output: Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka Anushka , because the * operator is used to repeat the string 'Anushka ' (with a space at the end) 10 times, resulting in 'Anushka ' repeated 10 times. Note that there is a space after 'Anushka' in the string, so when it is repeated, there will be a space between each occurrence of 'Anushka'.

#only multiplication and addition works with string, other arithmatic operators will give us error

"""multiplication for string is used to repeat the string a certain number of times, while addition is used for concatenation. Other arithmetic operators like subtraction (-), division (/), modulus (%), and exponentiation (**) are not defined for strings and will result in a TypeError if you try to use them with string operands."""

