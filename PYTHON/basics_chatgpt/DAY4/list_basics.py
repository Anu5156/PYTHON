# arr = [1, 2, 3, 4]
# print(arr[0])
# print(arr[-1])
# #output:1
# #output:4

# arr = [1, 2, 3]
# print(arr[3])
# #output:IndexError: list index out of range


# #LIST:mutable-->can be change throgh indexing
# a=[1,2,3,4,5,7]
# a[5] = 6
# print(a) #output:[1, 2, 3, 4, 5, 6]

# #list methods:
# arr = [3, 1, 2]
# arr.sort()
# print(arr)
#output: [1, 2, 3], because the sort() method sorts the list in place and returns None. To see the sorted list, you can print the list after calling sort():


a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)#output: [1, 2, 3]
print(b)#output: [1, 2, 3, 4]

a = [1, 2, 3]
b = a
b.append(4)
print(a)#output: [1, 2, 3, 4]
print(b)#output: [1, 2, 3, 4]
#here 'a' and 'b' are referencing the same list in memory, so changes made through 'b' will affect 'a' as well.
