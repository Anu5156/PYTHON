"""
WHAT IS RECURSION?
A function that calls itself to solve smaller subproblems
"""
# def func():
#     print("Hello")
# func()

# def print_n(n):
#     if n == 0:   # base case
#         return
#     print(n)
#     print_n(n-1)  # recursive call
# print_n(5)



# def func(n):
#     if n == 0:
#         return
#     func(n-1)
#     print(n)
#output: 1 2 3
# # func(3)

# def func(n):
#     if n == 0:
#         return
#     print(n)
#     func(n-1)
#     print(n)
# func(3)
# #output: 3 2 1 1 2 3

# def func(n):
#     if n == 0:
#         return
#     func(n-1)
#     print(n)
# func(1000000)


"""missing base case, will cause infinite recursion and eventually a stack overflow error"""
def func():
    func()

"""🧠 IMPORTANT CONCEPT

Stack memory is limited

👉 Python default limit ≈ 1000 recursive calls


✅ Option 1: Use iteration instead

👉 Replace recursion with loop

✅ Option 2: Increase limit (not recommended)
import sys
sys.setrecursionlimit(2000)"""


# def func(n):
#     return func(n-1)
# func(5)
# #RecursionError: maximum recursion depth exceeded


# def func(n):
#     if n == 0:
#         return 0
#     return func(n-1)

# func(5)
# #output: 0, because the base case returns 0 and all recursive calls eventually reach the base case.

# def func(n):
#     if n == 0:
#         return
#     return func(n-1)

# print(func(5))
# #output: None, because the base case returns None and all recursive calls eventually reach the base case.

# def func(n):
#     if n == 0:
#         return 1
#     return n * func(n-1)

# print(func(3))
# #output: 6, because func(3) = 3 * func(2) = 3 * (2 * func(1)) = 3 * (2 * (1 * func(0))) = 3 * (2 * (1 * 1)) = 6

# def func(n):
#     if n == 0:
#         return 1
#     print(n)
#     return n * func(n-1)

# func(3)
# #output: 3 2 1, because the function prints n before making the recursive call, so it prints 3, then 2, then 1 before reaching the base case.


# def func(n):
#     if n == 1:
#         return 1
#     return func(n//2) + func(n//2)

# print(func(4))
# #output: 4, because func(4) = func(2) + func(2) = (func(1) + func(1)) + (func(1) + func(1)) = (1 + 1) + (1 + 1) = 4

def func(n):
    if n == 1:
        return 1
    return func(n//2) + 1
print(func(8))

#google level question
def func(n):
    if n <= 1:
        return 1
    return func(n//2) + func(n//2) + 1
print(func(8))