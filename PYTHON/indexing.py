#INDEXING IN PYTHON: In python sequence like str are stored in continuous memory locations,we can access individual element/char of the string.
#each charcter in the memory locations is assigned a index which starts from 0 and ends at (len-1)
# """ex: str='Mayank'"""
"""FORWARD INDEXING: In python we can access the characters of the string using forward indexing, where the index starts from 0 for the first character and goes up to len-1 for the last character."""
# print(str[0])  # Output: M
# print(str[1])  # Output: a
# print(str[2])  # Output: y
# print(str[3])  # Output: a
# print(str[4])  # Output: n
# print(str[5])  # Output: k

"""BACKWARD INDEXING: In python we can also access the characters of the string using negative indexing, where the index starts from -1 for the last character and goes backwards to -len for the first character."""
# print(str[-1])  # Output: k, because negative indexing starts from the end of the string, so str[-1] gives us the last character 'k'.
# print(str[-2])  # Output: n, 
# print(str[-3])  # Output: a,
# print(str[-4])  # Output: y,
# print(str[-5])  # Output: a,
# print(str[-6])  # Output: M, 
# print(str[6])   # Output: IndexError: string index out of range, because the valid indices for the string 'Mayank' are from 0 to 5, and index 6 is out of range.




#lets print using loop
a="ANUSHKA"
print(a[len(a)-1]) #output: A, because a[len(a)-1] gives us the last character of the string 'ANUSHKA', which is 'A'.

# for i in range(0,len(a)): #using range
#     print(a[i])

# for i in a:
    #     print(i)
    
#output: A
#        N
#        U
#        S
#        H
#        K
#        A

#to print in reverse order:
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
#output: A
#        K
#        H
#        S
#        U
#        N
#        A


