import sys

# Define a list
lst = []

# Define a tuple
tpl = ()
print(type(tpl))
# Print the memory usage of the list
print("List memory usage:", sys.getsizeof(lst))

# Print the memory usage of the tuple
print("Tuple memory usage:", sys.getsizeof(tpl))

tpl1 = ''
print("Str size",sys.getsizeof(tpl1))

tpl11 = {}
print(type(tpl11))
print("Str size",sys.getsizeof(tpl11))