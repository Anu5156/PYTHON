d={"name1":"Anushka","name2":"Rohith","name3":"shalini"}
# for key in d.keys():
#     print(key)
# #output:
# # name1
# # name2
# #name3


# for val in d.values():
#     print(val)
# #output:Anushka
# # Rohith
# # shalini

# for k, v in d.items():
#     print(k, v)
# # output :
# name1 Anushka
# name2 Rohith
# name3 shalini

# d = {"a":1}
# print(d.get("b"))
# #output:None





# """🔹 6. IMPORTANT METHODS
# d.keys()
# d.values()
# d.items()
# d.get()
# d.pop()

# """

# # d = {"a":1, "b":2}

# # val = d.pop("a")

# # print(d)    # {'b': 2}
# # print(val)  # 1

# #safe way to pop:  d.pop(key, default_value)

# """d = {"a":1}

# print(d.pop("b", 0))   # 0 (no error)
# d.pop("b") #👉 ❌ KeyError if "b" not present"""

# # d.popitem() #👉 Removes last inserted key-value pair

# # d = {"a":1, "b":2}
# # d.popitem()
# # print(d)  
# # # {'a':1}

# d = {"a":1, "b":2}
# print(d.pop("c", 5))
# #output:5

# d = {"x":10, "y":20}
# print(d.popitem())
# #output:('y', 20)

# d = {"a":1}
# d.pop("b")
# #key-error


# s = "aabbbcc"
# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)
# #output:{'a': 2, 'b': 3, 'c': 2}

s="anushkaacharya"
freq={}
for ch in s:
  freq[ch]=freq.get(ch,0)+1
print(freq)
#output:{'a': 5, 'n': 1, 'u': 1, 's': 1, 'h': 2, 'k': 1, 'c': 1, 'r': 1, 'y': 1}



s = "programming"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq["g"])
#output:2

arr = [1,2,2,3,3,3]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)
#output:{1: 1, 2: 2, 3: 3}