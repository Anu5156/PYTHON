#logical operators:
#and, or, not

#and :It will return true when both conditions are true
#or:it will return true when at-least one of the conditions is true
#not:it will return true when the condition is false and it will return false when the condition is true


#EXAMPLE FOR AND OPERATOR:
a=40
b=20
c=50
print(a>b and c>b) #True #because both conditions are true
print(a>b and c<b) #False #because one condition is false
print(a>30 and b<30) #True #because both conditions are true
print(a>30 and b>30) #False #because one condition is false

#EXAMPLE FOR OR OPERATOR:
print(a>30 or b<30) #True #because at-least one condition is true
print(a>30 or b>30) #True #because at-least one condition is true
print(a<30 or b>30) #False #because both conditions are false



#EXAMPLE FOR NOT OPERATOR:
print(not(a>30)) #False #because the condition is true
print(not(a<30)) #True #because the condition is false

