#iterative statement/looping
"""Python provides the concept of looping .Looping/iteration is required when we need to execute a block of code/statement multiple times
A loop statement allows us to execute a group of statement /block multiple times """
"""In python ,it doesnot provide do while loop"""



"""while(condition):
        <indented statement>
        <indented statement>
        <indented statement>
    <non indented statement>
    <non indented statement>"""
# #ex:
# i=int(input("enter the number")) #start
# while(i<5):#here 5 is the end which wont include since we have used < only...
#     print(i)
#     i += 1
# """enter the number1
# 1
# 2
# 3
# 4"""

# #printing the first 10 natural numbers
# i=1
# while(i<10):
#     print(i)
#     i=i+1
"""1
2
3
4
5
6
7
8
9"""

#sum of the first 10 numbers
sum=0
i=1
while(i<=10):
    sum=sum+i
    i+=1
print(sum)#55


sum=0
i=1
while(i<=10):
    sum=sum+i
    i+=1
    print(sum)  
"""1
3
6
10
15
21
28
36
45
55
"""



