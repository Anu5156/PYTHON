#RELATIONAL OPERATOR IN PYTHON:
"""they are used to compare values."""
#they can either return TRUE or FALSE according to condition

#there are 6 relational operators in python:
a=10
b=20
print(a==b) #False
print(a!=b) #True
print(a> b) #False
print(a< b) #True
print(a>=b) #False
print(a<=b) #True

print(10>10)
#OUTPUT:
#False

"""Relational operators can be applied to strings,they give answer via LEXICOGRAPHICAL COMPARISION."""
print("apple"=="apple") #True
print("apple"!="apple") #False
print("apple">"apple") #False
print("apple"<"apple") #False
print("apple">="apple") #True
print("apple"<="apple") #True

#WHAT IS LEXIOGRAPHICAL COMPARISION?
#1.LOOP THROUGHINDIVIDUAL CHARACTER OF STRING
#ex:
a="small" 
b="big"  
print(a>b) #True #the number of characters in word small is greater than the number of the letter in word big

#2.get the unicode value and compare that.
ord("a")#97
ord("b")#98

print("apple">"banana") #False #because the unicode value of "a" is less than the unicode value of "b"

#ex2:
ord("s")#115
ord("S")#83
print("small">"Small") #True #because the unicode value of "s" is greater than the unicode value of "S"


#3.if the value is same continue,else the string whose characters UNICODE value is higher is bigger
print("apple">"apricot") #False #because the unicode value of "l" is less than the unicode value of "r"


print(ord("a"))
#output:97

print(ord("A")) #65

print(ord("!")) #33

#EXAMPLE:
b='!zzzzzzaaaaa'<'a'
print(b) #True #because the unicode value of "!" is less than the unicode value of "a"
##it checks only first character of string and gives answer according to that.

'aa'>='a'#True #because the unicode value of "a" is equal to the unicode value of "a"
'aa'>'a'#True #because the unicode value of "a" is greater than the unicode value of "a"
#as the unicode of the first character is same it checks the second character and gives answer according to that.


h = 'a'<'b'<'c' #chaining of relational operators
print(h) #True #because a is less than b and b is less than c

a=1<2<3
print(a) #True #because 1 is less than 2 and 2 is less than 3

v=1<2>3
print(v) #False #because 2 is greater than 3
#if any one condition is false the whole statement will be false

#special behavioue of relational operator:
"""
== :compares its operand for the equality for compatible type and same value and return true if they are equal.
!=   :compares for inequality and if the operands are not equal, it returns true; otherwise, it returns false. 
"""
#ex:
a=15==15.0
print(a) #True #because the value is same and compatible type

b=15=='15'
print(b) #False #because the value is different and incompatible type

c= True == 1
print(c) #True #because the value is same and compatible type

f= False == 0
print(f) #True #because the value is same and compatible type

j=0 == False
print(j) #True #because the value is same and compatible type

r=15!=15.0
print(r) #False #because the value is same and compatible type

k=15!='15'
print(k) #True #because the value is different and incompatible type

h= True == 'True'
print(h) #False #because the value is different and incompatible type
