#functions on list
"""
1.len() - returns the number of items in the list
2.max() - returns the largest item in the list
3.min() - returns the smallest item in the list
4.sum() - returns the sum of all items in the list
5.sorted() - returns a sorted list of the specified iterable
6.any() - returns True if any item in the list is true, otherwise returns False
7.all() - returns True if all items in the list are true, otherwise returns False
"""
li=[1,2,3,4,5]
print(len(li))
#output: 5
print(max(li))
#output: 5
print(min(li))
#output: 1
print(sum(li))
#output: 15
print(sorted(li))
#output: [1, 2, 3, 4, 5]
print(any(li))
#output: True
print(all(li))
#output: True
# print(len([]))
# #output: 0
# print(max([]))
# #output: ValueError: max() arg is an empty sequence
# print(min([]))
#output: ValueError: min() arg is an empty sequence

# l3=["abc",5]
# print(max(l3))
# #output: TypeError: '>' not supported between instances of 'int' and 'str'
# print(min(l3))
#output: TypeError: '<' not supported between instances of 'int' and 'str'

l6=["abc","zab","def"]
print(max(l6))
#output: zab
#The max() function compares the strings lexicographically (i.e., based on their Unicode code points) and returns the string that comes last in alphabetical order.
print(min(l6))
#output: abc
#The min() function compares the strings lexicographically and returns the string that comes first in alphabetical order.
# print(sum(l6))
#output: TypeError: unsupported operand type(s) for +: 'int' and 'str' 

l9=[5,9,3,0,1,2,4,7,9,6]
print(sorted(l9))
#output: [0, 1, 2, 3, 4, 5, 6, 7, 9, 9]

l0=[0]
print(any(l0))
#output: False

print(all(l0))
#output: False

l5=[None, False, 0, "", [], {}, set(),"abc"]
print(any(l5))
#output: True
print(all(l5))
#output: False
#if everything is true then it returns true otherwise false

"""Functions:called on an object or variable and perform a specific action on that object or variable. They are defined using the def keyword and can take arguments and return values.
ex:len(list), max(list), min(list), sum(list), sorted(list), any(list), all(list)
Methods: are functions that are associated with an object and can be called on that object. They are defined within a class and can access and modify the object's attributes. Methods are called using the dot 
notation, where the object is followed by a dot and the method name.
ex:
list.append()
list.remove()
list.sort()
list.reverse()
list.count()
list.index()
list.pop()
list.clear()
list.copy()
list.extend()"""

#append() method is used to add an item to the end of the list.
l1=[1,2,3]
l1.append(4)
print(l1)
#output: [1, 2, 3, 4]

#remove() method is used to remove the first occurrence of an item from the list.
l1.remove(2)
print(l1)
#output: [1, 3, 4]

# l1.remove(10)
#output: ValueError: list.remove(x): x not found

l1.sort()
print(l1)
#output: [1, 3, 4]

l1.reverse()
print(l1)
#output: [4, 3, 1]

print(l1.count(3))
#output: 1

print(l1.index(3))
#output: 1
l1.pop()
print(l1)
#output: [4, 3]

l1.clear()
print(l1)
#output: []

l2=[1,2,3]
l3=l2.copy()
print(l3)
#output: [1, 2, 3]

l2.extend([4,5])
print(l2)
#output: [1, 2, 3, 4, 5]

#if we want to add the elements to the first
#ex:
mylist = ["apple", "banana", "cherry"]
mylist.insert(0, "watermelon")
print(mylist)
#output: ['watermelon', 'apple', 'banana', 'cherry']

# mylist.insert("orange")
#output: TypeError: insert() takes exactly 2 arguments (1 given)

mylist.index("banana")
#output: 2
mylist.count("banana")
#output: 1

#speciality of remove() method is that it removes the first occurrence of the specified value.and everything will shift towards right side after the removed element.
l18=["apple", "banana", "cherry", "banana","chikku","pineapple","watermelon"]
l18.remove("banana")
print(l18)
#output: ['apple', 'cherry', 'banana','chikku','pineapple','watermelon']

if "banana" in l18:
    l18.remove("banana")
    print(l18)
#output: ['apple', 'cherry','chikku','pineapple','watermelon']

l18.pop()#removes the last element of the list and returns it.
print(l18)
#output: ['apple', 'cherry','chikku','pineapple']
print(l18.pop(1))#removes the element at the specified index and returns it.
#output: cherry

#you might be thinking why the original list is changed when you removed banana and cherry from the list. The reason is that both remove() and pop() methods modify the original list in place. When you call remove() or pop() on a list, it changes the list itself, rather than creating a new list with the changes. Therefore, when you print the list after calling these methods, you see the modified version of the original list.

#to return all the elements of the list in reverse order without modifying the original list we can use reversed() function.
l19=[1,2,3,4,5]
print(list(reversed(l19)))
#output: [5, 4, 3, 2, 1]

#to pop all the elements of the list we can use a while loop and pop() method until the list is empty.
l20=[1,2,3,4,5]
while l20:
    print(l20.pop())
#output:
#5
#4
#3
#2
#1

#clear() method is used to remove all the items from the list.
l21=[1,2,3,4,5]
l21.clear()
print(l21)
#output: []

l9=l2.copy()
print(l9)
#output: [1, 2, 3, 4, 5]

l9[0]=0
print(l9)
#output: [0, 2, 3, 4, 5]
#used to replace it with the new value but it does not change the original list l2.

#to add the elements at the first
l9.insert(0,0)
print(l9)
#output: [0, 1, 2, 3, 4, 5]

