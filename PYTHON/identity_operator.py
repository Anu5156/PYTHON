#identity operator: In Python, identity operators are used to compare the memory locations of two objects. There are two identity operators: "is" and "is not". The "is" operator returns True if both operands refer to the same object in memory, while the "is not" operator returns True if they do not refer to the same object.
"""They serve 2 purposes:
1.To verify if the reference point to the same memory location or not
2.To determine if the value is of certain class or type
"""

a=10
b=10
print(a is b) #True
print(a is not b) #False

print(id(a))#140711799878224
print(id(b))#140711799878224
#both the variable are pointing to the same location
c=1
print(id(c))#140711799878216
print(a is c) #False
print(a is not c) #True

#behaviour of is and is not
#is : it returns True if the operand are identical else false
#is not : it returns True if the operand are not identical else false

##here identical refers to the REFERENCE of the object in memory not the value of the object.
# EX:
a=10
b=10
print(a is b) #True
print(a is not b) #False

B='10'
print(B is int)#False
print(type(B))#<class 'str'>
print(type(B) is int) #False

#now what is the difference between the is and == operator?
#The "is" operator checks if two variables refer to the same object in memory, while the "==" operator checks if the values of the variables are equal.
a=10
b=10
print(a is b) #True
print(a == b) #True

l1=[[1],[2],[3]]
l2=[[1],[2],[3]]
print(id(l1))#1447314877376
print(id(l2))#1447315305984
print(l1==l2)
#output:True

print(l1 is l2)
#output:False


