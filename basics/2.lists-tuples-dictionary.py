#--- 1. LISTS ---#
list = ["abc", "jhi", "lmn", "pqr", "xyz"]

print(list[3])              # item at index
print(list[-3])             # item from last (3rd last)
print(list[2:4])            # subset of items from 3rd item to 4th item
print(list[2:])             # subset from 3rd item to last item
print(list * 2)             # prints list 2 times
print(list + ["uvw"])       # concat list with another list
print("xyz" in list)        # find in list

list[1] = "pqr"
list[1:2] = ["ijk", "lmn"]  # update a range of items

list.insert(1, "rst")       # list functions
list.remove("abc")
list.sort()
copy = list.copy()

#--- 2. TUPLES (A tuple is a read only list which is ordered and unchangeable) --#
tup = ("abc", 123, 45.6, "pqr", "xyz")

print(tup[3])               # item at index
print(tup[2:4])             # subset of items from 3rd item to 4th item
print(tup[2:])              # subset from 3rd item to last item
print(tup * 2)              # prints tuple 2 times
print(tup + ("123", 456))   # concat tuple with another tuple

list[2] = 12        # valid syntax
# tup[2] = 12       # invalid syntax

#--- 3. SET (A set is a collection which is unordered, unchangeable, and un-indexed) ---#
set = {"apple", "banana", "cherry"}  # set does not allow duplicates
print(set)

print("banana" in set)      # access set items
set.add("orange")           # cannot be changed, only new items are added
set.remove("banana")

#--- 4. DICTIONARY (Dictionaries are used to store data values in key:value pairs) --#
dict1 = {}
dict2 = {123: "John Doe", "role": "designer"}  # init a dictionary

print(dict1)
print(dict2)

dict1['John'] = "45,000"  # add key value pair to dictionary
print(dict1)

print(dict1["John"])
print(dict2[123])
print(dict2.get("role"))

print(dict1.keys())     # get keys of a dict
print(dict2.values())   # get values of a dict
