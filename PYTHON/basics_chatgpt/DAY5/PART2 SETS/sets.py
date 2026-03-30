#SETS:collection of unique elements

# s = {1,2,3,3}
# print(s)
# #output:{1,2,3}

# s.add(4)
# print(s)

# s.remove(5)
# print(s)
# #keyerror

# s = {1,2,3}
# s.add(2)
# print(s)
# #output:{1,2,3}


a = {1,2,3}
b = {3,4,5}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
#output:
"""{1, 2, 3, 4, 5}
{3}
{1, 2}
"""

