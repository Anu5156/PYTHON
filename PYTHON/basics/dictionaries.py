# Dictionaries = a collection of key-value paired ordered and changeable.No deuplicates

capitals={"USA":"Washington DC",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"
                     }
# print(dir(capitals))
print(capitals)
print(type(capitals))
# to get only value of USA
print(capitals["USA"])
# to update the value of USA
capitals["USA"]="Las Vegas"
print(capitals)
# to remove the key-value pair of USA
capitals.pop("USA")
print(capitals)
#to display only keys
print(capitals.keys())

#to display only values
print(capitals.values())

#to print one after the other in coloumns..
for key,value in capitals.items():
    print(key,value)