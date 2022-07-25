#--- VARIABLES AND DATA TYPES ---#
x = "Hello World"                   # string
x = 20                              # int
x = 20.5                            # float
x = 1j                              # complex
x = ["apple", "banana", "cherry"]   # list
x = ("apple", "banana", "cherry")   # tuple
x = range(6)                        # range
x = {"name": "John", "age": 36}     # dict
x = {"apple", "banana", "cherry"}   # set
x = frozenset({"apple", "banana", "cherry"})    # frozenset
x = True                            # bool
x = b"Hello"                        # bytes
x = bytearray(5)                    # bytearray
x = memoryview(bytes(5))            # memoryview
x = None                            # none type

#--- TYPE CASTING ---#
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#--- GET DATA TYPE OF VARIABLES ---#
print(type(x) == int)       # false
print(type(x) == str)       # true

#--- DELETE VARIABLE REFERENCE ---#
del x

#--- GLOBAL VARIABLES ---#
global_var = "This is global!"


def main():
    print(global_var)

    global var      # using global keyword
    var = "This is also global!"


main()
print(var)

#--- STRING ---#
str = "Hello World!"

len = len(str)                  # length of string
print("Hell" in str)            # check substring
print("Hello" not in str)       # check not in substring

print(str[1])                   # character at index
print(str[2:])                  # substring from 3rd char to last char
print(str[1:6])                 # substring from 2nd char to 6th char
print(str[-5:-2])               # from 5th char from end to 2nd last char

print(str.lower())              # converts string to lower case
print(str.upper())              # converts string to upper case
print("   Hello!   ".strip())   # removes trailing spaces
print("Hello!" + "World")       # concat string

print("Hi {} your bill is ${}".format("John", "36.66"))     # formatting string
