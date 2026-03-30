i = 0
while i < 5:
    print(i)
    i += 1
#output:0,1,2,3,4

#👉 What happens if increment is missing?->output:0 several times


i = 5
while i:
    print(i)
    i -= 1
#output:5,4,3,2,1