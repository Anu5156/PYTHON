
# #A lambda function is a small anonymous function defined using the lambda keyword.
# """syntax:
# lambda arguments: expression
# """

# add = lambda a, b: a + b
# print(add(2, 3))

# x = lambda a: a * 2
# print(x(5))
# #output:10

# #normal function:
# def square(x):
#     return x * x
# print(square(4))

# #lambda function:
# square = lambda x: x * x
# print(square(6))

# #Even or odd
# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check(5))

# #maximum of two numbers
# num=lambda a,b:"MAX" if a>b else "MIN"
# print(num(10,20))

# #string uppercase
# f = lambda s: s.upper()
# print(f("rohith"))
# #output:ROHITH

# #lenght of the string
# length = lambda s: len(s)
# print(length("Hello, World!"))
# #output:13

#🔥 ADVANCED (IMPORTANT FOR INTERVIEWS)
# nums = [1, 2, 3, 4]
# res = list(map(lambda x: x * 2, nums))
# print(res)
# #output:[2, 4, 6, 8]

# nums = [1, 2, 3, 4, 5]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)
# #output:[2, 4]

#sorting
# points = [(1, 2), (3, 1), (5, 4)]
# points.sort(key=lambda point: point[0])
# print(points)
# #output:[(3, 1), (1, 2), (5, 4)]

# #sorting in reverse order
# points.sort(key=lambda point: point[1], reverse=True)
# print(points)

arr = [(1, 3), (2, 1), (5, 0)]
print(sorted(arr, key=lambda x: x[1]))
print(arr)


arr = [(1, 3), (2, 1), (5, 0)]
arr2 = arr.sort(key=lambda x: x[1])
print(arr2) #none
print(arr) #[(5, 0), (2, 1), (1, 3)]