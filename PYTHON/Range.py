#Range()function:it is an inbuilt function in python and it returns a range object
#The range function is very useful to generate a sequence of numberss which can be casted into sequence (list,tuple)
"""the range()function takes 1 to 3 arguments"""

#1.Range with one parameter
"""range(n):returns a range object containing integer value from 0 to n-1"""

a=range(5)
print(a)
#range(0, 5)

type(a)#range

#we will cast it to list
li=list(a)
print(li)#[0, 1, 2, 3, 4]

#direct cast
print(list(range(10)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#basically the range starts from 0 and ends at n-1

# print(list(range(-3)))
#[]
#Range of the negative number is empty list or empty
#Range is coded in sucha way that it moves right side with the start value 0



#Range with 2 parameters
#range(start,stop)
"""we will get a range object containing integr values from start to end-1(n-1)"""
#ex:
# a=range(0,5)
# print(a)

# print(tuple(range(0,5)))
#(0, 1, 2, 3, 4)
print(set(range(1,10)))
#{1, 2, 3, 4, 5, 6, 7, 8, 9}

#ex1:
print(list(range(10,1)))
#output:[]
#from above example we came to know that always range starts from smaller number to bigger number(only applicable is step size is not given)
#ex2:
print(list(range(-10,-5)))
#[-10, -9, -8, -7, -6]

#ex3:
print(list(range(-3,-10)))
#[]

print(list(range(-3,-3)))
#[]

#Range function with 3 parameters
#syntax:
# range(start.stop,step)
#Range acts similar to slicing

print(list(range(0,10,2)))
#output:[0, 2, 4, 6, 8]
#it prints all the even number from 0t0 10 excluding 10
#0 is the start
#10 is the stop
#2 is the step
#here,step will stop at 10-2=8 ==>stop-step 

print(list(range(3,9,-1)))
#output:[]
#since step is negative,we cant subtract 3+(-1)=2 but start is from 3..

print(list(range(7,1,-2)))
#output:[7,5,3] though 3-2=1 stop number is excluded that's why 1 is not included in the output

print(list(range(5,10,15)))
#output:[5]
#here it only,prints 5 and doenot prints further since the step size is out of range i.e:stop

print(list(range(3,-9,-1)))
#[3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]

print(list(range(1,10,int(1.5))))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(range(1,10,1.5)))
#since the step size is floating integer

# print((list(range(1.5,10.5,0.5))))
#TypeError: 'float' object cannot be interpreted as an integer 

# print(list(range(0,5,0)))
#ValueError: range() arg 3 must not be zero

print(list(range(2,12)))
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


print(list(range(12,2)))
#[]
#none of the arguments in the range must be floating value


"""
1.Using Range with for-loop:
We can use range() and for together for iterarting through a list of numeric values.
syntax:
    for<var_name> in range(num):
        <indented statement 1>
        <indented statement 2>
        <indented statement 3>
  
              """
for num in range(0,10,2):
    print(num)
#output:
#0
#2
#4
#6
#8

for num in (list(range(0,10,2))):
    print(num)
#output:0
# 2
# 4
# 6
# 8

#WAP to take a number from the user and display sum of all numbers from 1 to that numbers
# num=int(input("Enter the number:"))
# sum=0
# for i in range(0,num+1):
#     sum=sum+num
# print(sum)
#Enter the number:5
# 30

#WAP to take a number from user and find its factorial
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i 
print(fact)
#Enter the number:3
#6