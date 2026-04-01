#Assignment operator
"""Python assignment operator is used to assign values to declared values"""
#(=)is the assignment operator in python.

a=10
b=True
d,e,f="apple","banana","grapes"
print(a) #10
print(b) #True
print(d,e,f) #apple ,banana ,grapes

s,t,u=2
print(s,t,u)
#  s,t,u=2
#     ^^^^^
# TypeError: cannot unpack non-iterable int object

#compound assignment operator:
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
a>>=2 #a=a>>2
print(a) #0.0
a<<=2 #a=a<<2
print(a) #0.0
a&=2 #a=a&2
print(a) #0.0
a|=2 #a=a|2
print(a) #2.0


#python doesnot have the increement operator like (++) and decrement operator like (--) as in other programming languages.
