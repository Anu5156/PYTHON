#Madlibs game(a word game where you fill in the blanks to create a funny story)

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
story = f"""Once upon a time in a {adjective1} land, there was a {adjective2} {noun1}.
Every day, it would {verb1} with its best friend, a {noun2}.
One day, they decided to visit a {animal} at the {place}.
They had so much fun that they couldn't stop {verb2} all the way home!"""
print(story)
