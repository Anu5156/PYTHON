#List in python=[]:
"""A list is a collection which is ordered and changeable. In Python lists are written with square brackets."""
#ex:
thislist = ["apple", "banana", "cherry"]
print(thislist)
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#list characteristics:
"""
1. Ordered: The items have a defined order, and that order will not change unless you explicitly reorder the list.
2. Changeable: You can change, add, and remove items in a list after it has been created.
3. Allow Duplicates: Since lists are indexed, they can have items with the same value.
4. Heterogeneous: A list can contain items of different data types, including other lists.
 #ex:
mylist = ["apple", 1, True, 3.14, [1, 2, 3]]
#output: ['apple', 1, True, 3.14, [1, 2, 3]]
5. Dynamic: The size of a list can change dynamically as you add or remove items.
6. Mutable: Lists are mutable, meaning you can modify them after they have been created.
#ex:
mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)
#output: ['apple', 'blackcurrant', 'cherry']

7. Iterable: You can iterate through the items in a list using loops.
8. Nesting: Lists can contain other lists, allowing for the creation of complex data structures.
9. Built-in Methods: Python provides a variety of built-in methods for lists, such as append(), remove(), pop(), and sort(), which allow you to manipulate the list easily.
10. Slicing: You can access a range of items in a list using slicing, which allows you to create sublists.
11. Indexing: You can access individual items in a list using their index, which starts at 0 for the first item.
12. Negative Indexing: You can also use negative indexing to access items from the end of the list, where -1 refers to the last item, -2 to the second last item, and so on.
13. List Comprehension: Python supports list comprehension, which provides a concise way to create lists based on existing lists or iterables.
14:Allow duplications: Since lists are indexed, they can have items with the same value."""
#ex:
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)
#output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

"""CREATING A LIST:
You can create a list by placing all the items (elements) inside square brackets [], separated by commas.
PRINT A LIST:
You can print the list using the print(list()) function.
ACCESSING ITEMS:
You can access the list items by referring to the index number, inside square brackets [].
Note: The first item has index 0, the second item has index 1 etc.
Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.
LIST SLICING:
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items."""

l4=list(("apple", "banana", "cherry"))
print(l4)
#output: ['apple', 'banana', 'cherry']

l6=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(l6[2:5])
#output: ['cherry', 'orange', 'kiwi']
print(l6[:4])
#output: ['apple', 'banana', 'cherry', 'orange']
print(l6[2:5])
#output: ['cherry', 'orange', 'kiwi']
print(l6[2:5:1])
#output: ['cherry', 'orange', 'kiwi']
print(l6[2:5:2])
#output: ['cherry', 'kiwi']

"""SLICING AND INDEXING:
You can use slicing to access a range of items in a list. The syntax for slicing is"""
#list[start:stop:step]

L3=["apple", 12,3.14,[1,1,1],True]
print(L3[0])
#output: apple
print(L3[1])
#output: 12
print(L3[2])
#output: 3.14
print(L3[3])
#output: [1, 1, 1]
print(L3[4])
#output: True
print(L3[-1])
#output: True
print(L3[-2])
#output: [1, 1, 1]
print(L3[-3])
#output: 3.14
print(L3[-4])
#output: 12
print(L3[-5])
#output: apple
print(L3[1:4])
#output: [12, 3.14, [1, 1, 1]]
print(L3[:4])
#output: ['apple', 12, 3.14, [1, 1, 1]]
print(L3[2:])
#output: [3.14, [1, 1, 1], True]
print(L3[::2])
#output: ['apple', 3.14, True]
print(L3[1:4:2])
#output: [12, [1, 1, 1]]
#list operations:
"""
1. Concatenation: You can concatenate two lists using the + operator.
2. Repetition: You can repeat a list a specified number of times using the * operator.
3. Membership: You can check if an item is in a list using the in keyword.
4. Length: You can get the number of items in a list using the len() function.
5. Iteration: You can iterate through the items in a list using a for loop.
6. Slicing: You can access a range of items in a list using slicing.
7. Indexing: You can access individual items in a list using their index.
8. Negative Indexing: You can access items from the end of the list using negative indexing.
9. List Comprehension: You can create new lists based on existing lists using list comprehension.
10. Built-in Methods: Python provides various built-in methods for lists, such as append(), remove(), pop(),
sort(), and reverse(), which allow you to manipulate the list easily.
11. Nesting: Lists can contain other lists, allowing for the creation of complex data structures.
12. Mutability: Lists are mutable, meaning you can modify them after they have been created.
13. Dynamic Sizing: The size of a list can change dynamically as you add or remove items.
14. Heterogeneous: A list can contain items of different data types, including other lists.
15. Allow Duplicates: Since lists are indexed, they can have items with the same value.
16. Ordered: The items have a defined order, and that order will not change unless you explicitly reorder the list.
17. Iterable: You can iterate through the items in a list using loops.
18. Slicing and Indexing: You can use slicing to access a range of items in a list, and indexing to access individual items.
19. List Comprehension: Python supports list comprehension, which provides a concise way to create lists based on existing lists or iterables."""

#modifying list:
mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)
#output: ['apple', 'blackcurrant', 'cherry']

#to add an element from the end of the list use append() method:
mylist.append("orange")
print(mylist)
#output: ['apple', 'blackcurrant', 'cherry', 'orange']

#to add an element at a specified position use insert() method:
mylist.insert(1, "watermelon")
print(mylist)
#output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange']

#merge two lists use extend() method:
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)
#output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

#to concatenate two lists use + operator:
list = mylist + tropical
print(list)
#output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'mango', 'pineapple', 'papaya']

#repeatation of list use * operator:
repeated_list = mylist * 2
print(repeated_list)
#output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

#Membership test use in keyword:
print("apple" in mylist)
#output: True

print("grape" in mylist)
#output: False

#iterable:
for item in mylist:
    print(item)
#output:
#apple
#watermelon
#blackcurrant
#cherry
#orange
#mango
#pineapple
#papaya
"""It prints each item in the list on a new line,one by one"""

L3=["apple", 12,3.14,[1,1,1],True]
for ele in L3:
    print(ele)
#output: apple
#output: 12
#output: 3.14
#output: [1, 1, 1]
#output: True

print("12" in L3)
#output: False
#since 12 is the number not a string, it returns False
