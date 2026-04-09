# name="Anushka" 
# for ch in name:
#     print(ch)
#output:
"""
A
n
u
s
h
k
a
"""
l1=[1,2,3,4,5]#list
# for num in l1:
#     print(num)
#output:
"""
1
2
3
4
5
"""
# start=0
# while(start <len(l1)):
#     print(l1[start])
#     start=start + 1

#write a program to take a string and output all char except vowels
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for ch in list:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
"""
b
c
d
f
g
h
j
k
l
m
n
p
q
r
s
t
v
w
x
y
z"""



