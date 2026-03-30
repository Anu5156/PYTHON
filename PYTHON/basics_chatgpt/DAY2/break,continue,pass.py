#break
for i in range(5):
    if i == 3:
        break
    print(i)
#output:0,1,2, because when i becomes 3 loop breaks and it does not print 3,4

#continue
for i in range(5):
    if i == 3:
        continue
    print(i)
#output:0,1,2,4 because when i becomes 3 it does not print 3 and continues to next iteration and prints 4

#pass
for i in range(5):
    if i == 3:
        pass
    print(i)
#output:0,1,2,3,4 because when i becomes 3, pass does nothing and continues to next iteration



for i in range(5):
    if i == 2:
        continue #output:0,1,3,4
    if i == 4:
        break #output:0,1,3 because when i becomes 4 loop breaks and it does not print 4
    print(i)
    #final output:0,1,3 because when i becomes 2 it does not print 2 and continues to next iteration and when i becomes 4 loop breaks and it does not print 4
    