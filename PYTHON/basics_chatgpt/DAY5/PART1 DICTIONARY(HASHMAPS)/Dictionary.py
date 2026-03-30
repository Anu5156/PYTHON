# #dictionary:it stores data in key value pairs
# a={1:"one",2:"two",3:"three"}
# print(a)
# print(type(a))
# #{1: 'one', 2: 'two', 3: 'three'}
# # <class 'dict'>

# student = {
#     "name": "Anushka",
#     "age": 20
# }
# print(student)
# # {'name': 'Anushka', 'age': 20}

"""🧠 KEY PROPERTIES
Keys must be unique
Keys must be immutable (string, int, tuple)
Values can be anything"""

d = {1: "a", 1: "b"}
print(d)
# {1: 'b'}

d = {"a":1, "b":2, "a":3}
print(d)
# {'a': 3, 'b': 2}

d = {True: "yes", 1: "no"}
print(d)
# {True: 'no'}

"""ACCESSING VALUES:"""
d = {"name": "Anushka", "age": 20}
print(d["name"])

print(d.get("name"))

"""🧠 INTERVIEW DIFFERENCE
Method	Behavior
d[key]	error if missing
d.get(key)	safe if missing, returns None or default value"""
