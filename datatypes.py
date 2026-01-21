# TEXT TYPE
name = "Alice"               # str

# NUMERIC TYPES
age = 25                     # int
height = 5.4                 # float
complex_number = 2 + 3j      # complex

# SEQUENCE TYPES
fruits = ["apple", "banana", "cherry"]   # list
coordinates = (10, 20)                   # tuple
numbers = range(5)                       # range

# MAPPING TYPE
person = {"name": "Alice", "age": 25}    # dict

# SET TYPES
unique_numbers = {1, 2, 3, 3}            # set
fixed_set = frozenset([4, 5, 6])         # frozenset

# BOOLEAN TYPE
is_active = True                         # bool

# BINARY TYPES
byte_data = b"Hello"                     # bytes
byte_array = bytearray([65, 66, 67])     # bytearray
memory_view_data = memoryview(byte_data) # memoryview

# PRINT ALL VALUES WITH TYPES
print(type(name), name)
print(type(age), age)
print(type(height), height)
print(type(complex_number), complex_number)
print(type(fruits), fruits)
print(type(coordinates), coordinates)
print(type(numbers), list(numbers))
print(type(person), person)
print(type(unique_numbers), unique_numbers)
print(type(fixed_set), fixed_set)
print(type(is_active), is_active)
print(type(byte_data), byte_data)
print(type(byte_array), byte_array)
print(type(memory_view_data), memory_view_data)
