for i in range(5):
    print(i)
#output: 0 1 2 3 4 =5 numbers but it starts from 0 and ends at 4
#👉 What does range(5) actually return internally?
"""
r = range(5)
print(r)
#output: range(0, 5) → it is a sequence of numbers starting from 0 to 4"""

print(list(range(5)))
#output: [0, 1, 2, 3, 4] → list of numbers from 0 to 4

range(1000000000)
#output: range(0, 1000000000) → it does not create a list of 1000000000 numbers but it creates a range object which is an iterable and it generates numbers on the fly when we iterate over it

list(range(1000000000))
#memory error 

"""how does range generates the sequence:
range(start, stop, step)"""

for i in range(1, 5):
    print(i)#output: 1,2,3,4
    