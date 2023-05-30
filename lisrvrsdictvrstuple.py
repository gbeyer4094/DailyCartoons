#arrays
# Creating an array (list)
my_array = [1, 2, 3, 4, 5]

# Accessing elements in the array
print("Element at index 0:", my_array[0])
print("Element at index 2:", my_array[2])
print("Elements in reverse:", my_array[::-1])
print("Elements in 1-3:", my_array[1:4])

# Modifying an element in the array
my_array[3] = 10
print("Modified array:", my_array)

# Appending an element to the array
my_array.append(6)
print("Array after appending 6:", my_array)

# Removing an element from the array
my_array.remove(2)
print("Array after removing 2:", my_array)

# Checking the length of the array
array_length = len(my_array)
print("Length of the array:", array_length)

# Iterating over the array
print("Elements in the array:")
for element in my_array:
    print(element)

#dictionary
# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing values in the dictionary
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Modifying a value in the dictionary
my_dict["age"] = 35
print("Modified dictionary:", my_dict)

# Adding a new key-value pair to the dictionary
my_dict["occupation"] = "Engineer"
print("Dictionary after adding occupation:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict["city"]
print("Dictionary after removing city:", my_dict)

# Checking if a key is present in the dictionary
is_present = "name" in my_dict
print("Is 'name' present in the dictionary?", is_present)

# Getting the number of key-value pairs in the dictionary
dict_length = len(my_dict)
print("Number of key-value pairs in the dictionary:", dict_length)

# Iterating over the dictionary
print("Key-value pairs in the dictionary:")
for key, value in my_dict.items():
    print(key + ":", value)

#tuple
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in the tuple
print("Element at index 0:", my_tuple[0])
print("Element at index 2:", my_tuple[2])

# Attempting to modify an element (Tuples are immutable)
# my_tuple[3] = 10  # This line will raise a TypeError

# Checking the length of the tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# Iterating over the tuple
print("Elements in the tuple:")
for element in my_tuple:
    print(element)

#set
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding elements to a set
my_set.add(6)
my_set.add(7)
print("Set:", my_set)

# Removing an element from a set
my_set.remove(3)
print("Set:", my_set)

# Checking if an element is in the set
is_present = 5 in my_set

# Getting the length of a set
set_length = len(my_set)

# Printing the set and its properties
print("Set:", my_set)
print("Is 5 present in the set?", is_present)
print("Length of the set:", set_length)