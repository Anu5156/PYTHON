# for ch in "abc":
#     print(ch)
# #output:a
#         #:b
#         #:c

# s = "abc"
# for i in range(len(s)):
#     print(s[i])
# #output:a
#         #:b
#         #:c

# #Palindorme:
# s = "madam"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# #2 pointer approach:
# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1

#     return True


# print(is_palindrome("madam"))   # True
# print(is_palindrome("hello"))   # False

#not suitable for interview
def func(s):
    return s == s[::-1]

s = input("Enter a string: ")
print(func(s))