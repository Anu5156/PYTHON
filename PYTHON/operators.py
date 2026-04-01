#operators are special symbols that carry out different  kinds of computional on values
#there are different types of operations that python supports
#operator are special symbol in python which can manipulate the value of python
#1. Arithmetic operators: +, -, *, /, //, %, **
#2. Comparison operators: ==, !=, 0>, <, >=, <=
#3. Logical operators: and, or, not
#4. Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
#5. Bitwise operators: &, |, ^, ~, <<, >>
#6. Identity operators: is, is not
#7. Membership operators: in, not in
#8. Ternary operator: if-else
#9. Walrus operator: :=
#10. Augmented assignment operator: +=, -=, *=, /=, //=, %=, **=

#ARITMATIC OPERATORS:
a=10
b=3
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a//b) #floor division
print(a%b) #modulus very imp
print(a**b) #exponentiation
#OUTPUT:
#13
#7
#30
#3.3333333333333335
#3
#1
#1000
#In the above example, we have used different arithmetic operators to perform various operations on the values of a and b. The output shows the result of each operation.

#COMPARISON OPERATORS:
x=5
y=10
print(x==y) #equal to
print(x!=y) #not equal to
print(x>y) #greater than
print(x<y) #less than
print(x>=y) #greater than or equal to
print(x<=y) #less than or equal to
#OUTPUT:
#False
#True
#False
#True
#False
#True

#LOGICAL OPERATORS:
p=True
q=False
print(p and q) #logical AND
print(p or q) #logical OR
print(not p) #logical NOT
#OUTPUT:
#False
#True
#False

#ASSIGNMENT OPERATORS:
a=10
a+=5 #a=a+5
print(a) #15
a-=3 #a=a-3
print(a) #12
a*=2 #a=a*2
print(a) #24
a/=4 #a=a/4
print(a) #6.0
a//=2 #a=a//2
print(a) #3.0
a%=2 #a=a%2
print(a) #1.0
a**=3 #a=a**3
print(a) #1.0

#BITWISE OPERATORS:
x=5 #binary: 0101
y=3 #binary: 0011
print(x & y) #bitwise AND: 0001 (1)
print(x | y) #bitwise OR: 0111 (7)
print(x ^ y) #bitwise XOR: 0110 (6)
print(~x) #bitwise NOT: 1010 (-6)
print(x << 1) #left shift: 1010 (10)
print(x >> 1) #right shift: 0010 (2)
#OUTPUT:
#1
#7
#6
#-6
#10
#2

#IDENTITY OPERATORS:
a=10
b=10
print(a is b) #True
print(a is not b) #False
#OUTPUT:
#True
#False

#MEMBERSHIP OPERATORS:
my_list=[1, 2, 3, 4, 5]
print(3 in my_list) #True
print(6 in my_list) #False
print(3 not in my_list) #False
print(6 not in my_list) #True
#OUTPUT:
#True
#False

#TERNARY OPERATOR:
age=18
status="Adult" if age>=18 else "Minor"
print(status) #Adult
#OUTPUT:
#Adult

#WALRUS OPERATOR:
#The walrus operator (:=) allows you to assign a value to a variable as part of an expression. It is useful for reducing the number of lines of code and improving readability.
#Example:
n=5
if (s:=n**2) > 20:
    print(f"The square of {n} is greater than 20: {s}")
else:
    print(f"The square of {n} is not greater than 20: {s}")
#OUTPUT:
#The square of 5 is greater than 20: 25

#Augmented Assignment Operator:
x=10
x+=5 #x=x+5
print(x) #15
x-=3 #x=x-3
print(x) #12
x*=2 #x=x*2
print(x) #24
x/=4 #x=x/4
print(x) #6.0
x//=2 #x=x//2
print(x) #3.0
x%=2 #x=x%2
print(x) #1.0
x**=3 #x=x**3
print(x) #1.0
#OUTPUT:
#15
#12
#24
#6.0
#3.0
#1.0
#1.0
#In the above example, we have used different operators to perform various operations on the values of a, b, x, and y. The output shows the result of each operation.

