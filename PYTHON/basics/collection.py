#collection= This module demonstrates the use of various collection data types in Python.
"""N1) Lists: Ordered, mutable collections of items.
    2) Tuples: Ordered, immutable collections of items.
    3) Sets: Unordered collections of unique items."""

"""----lists----"""
# fruits = ['apple', 'banana', 'cherry','orange', 'kiwi','melon']
# print("Original list:", fruits)
"""--To print length of list---"""
# print("Length of list:", len(fruits))
# #to access elements by index
# print("First fruit:", fruits[0])#apple
# print(fruits[::-1])#reverse list
# #to add elements
# fruits.append('grape')#adds grape at the end
# print("After appending grape:", fruits)

# for x in fruits:
#     print(x)

# print(dir(fruits)) # give the list of all methods available for list object
# print(help(fruits))
"""-------------------------------------------"""
# to check whether the item is present in the list or not
##1st method
# if 'banana' in fruits:
#     print("Banana is present in the list")

# ##2nd method
# print("kiwi" in fruits) #true
# print("papaya" not in fruits) #true
"""-------------------------------------------"""
#reassigning value at specific index
# fruits[1] = 'blackcurrant' #banana is replaced by blackcurrant
# fruits.remove('orange') #removes orange from the list
# fruits.sort() #sorts the list in ascending order
# fruits.insert(2, 'watermelon')# inserts watermelon at index 2
# fruits.reverse()#reverses
# fruits.pop() #removes the last item
# fruits.extend(['papaya', 'mango']) #adds multiple items to the list

# print(fruits)




"""-----------------Sets---------------------------"""
# # Sets are unordered collections of unique elements
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# # print("Set1:", set1)
# # print("Set2:", set2)
# # print("Union:", set1.union(set2)) # combines elements from both sets
# # print("Intersection:", set1.intersection(set2)) # common elements

# fruits={'apple','banana','coconut','dragon fruit','coconut'}
# # fruits.remove("apple")
# print(fruits)#{'apple', 'banana', 'coconut', 'dragon fruit'}
# # fruits.add("pineapple")
# # print(fruits)
# # fruits.pop()
# # print(fruits)
# # fruits.clear()
# # print(fruits)
# # *sets cannot have duplicate valus...





"""-------------------TUPLES--------------------------"""
fruits=("apple","orange","coconut","banana","chikku","pineapple")
print(fruits)
# len(fruits)
# print(fruits)
# fruits.count("apple")
# print(fruits)
print(fruits.index("apple"))
print(fruits.count("pineapple"))
