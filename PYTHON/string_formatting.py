#string formatting allows us to create DYNAMIC STRINGS keys combining (plugging in) values an variables in them

#it is also used in print statement where we pass string
# there are 3 types of formatting string method
#1.Formatting with % operator
#2.Formatting with format() method
#3.f-string


#1.Formatting with % operator
s1="Mayank"
print("my name is:",(s1))
#output:my name is: Mayank

#2.Formatting with format() method
s2="Anushka"
print("My name is %s" %(s2))
print("Hi %s,I am %s" %(s2,'Anushka'))
# My name is Anushka
# Hi Anushka,I am Anushka

"""%d:integer
    %s:string
    %f:float"""

#ex1:
a="HELLO"
b="WORLD"
print("I have printed %s %s in python!"%(a,b))
#I have printed HELLO WORLD in python!

#precision handling with % operator
#Floating point number use the format %w.p(whole,precision)
print("the number is %2.3f"%(3.1415))
#output:the number is 3.142
# .3 represents the rounding up of value after the decimal point from 3 positions


res=10/3
print(res)#output:3.33333333333335
print("The result is %2.5f" %(res))#3.33333
print("the result is %2.1f" %(res))#3.3

res1=10/8
print(res1)
print("The result is %2.1f" %(res))#output:1.2

pi=3.141592653589793
print("The value pf pi rounded to 2 decimal place is %.2f" %pi)#output:3.14
print("The value of pi rounded to 3 decimal places is {:.3f}" .format(pi))
#output:
print(f"The value of pi rounded to 4 decimal places is {pi:.4f}")
"""The value pf pi rounded to 2 decimal place is 3.14
The value of pi rounded to 3 decimal places is 3.142
The value of pi rounded to 4 decimal places is 3.1416"""

name2="Anushka"
age1=19
print("My name is {} and I am {} years old".format(name2,age1))
#My name is Anushka and I am 19 years old

#Positional Arguments
print("My name is {0} and My age is {1}" .format(name2,age1))
#My name is Anushka and My age is 19 

#Named Arguments
print("Hello {name} , you are {age} years old" .format(name=name2,age=age1))
#Hello Anushka , you are 19 years old

#Python F-string
#it makes string formatting very easy and efficient then previous method.
#syntax:f'Hello {name} , welcome to {s1}'
#ex:
firstname="Anushka"
secondname="Acharya"
str3=f"Hello my first name is {firstname} and my surname is {secondname}"
print(str3)
#output:Hello my first name is Anushka and my surname is Acharya

income=100
tax=20
print(f"My final income is {income-tax}")
#My final income is 80

#{value:{width}.{precision}}
pie=3.1415567623
print(f"The value of pie is :{pie:{1}.{5}}")
#The value of pie is :3.1416