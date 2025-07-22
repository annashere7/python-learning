"""
This script demonstrates the basic operations of sets in Python.
Sets are unordered collections of unique elements. The following properties
are associated with sets:

1. Unordered: The elements in a set do not have a defined order.
2. Unique: A set cannot contain duplicate elements.
3. Mutable: Sets can be modified after their creation (elements can be added or removed).
4. Iterable: Sets can be iterated over.
5. Dynamic: Sets can grow and shrink in size as elements are added or removed.
"""
s=set()
print("Initial set:",type(s)) #empty set
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Checking if an element is in the set
print("Is 2 in the set?", 2 in my_set)

# Set union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print("Union of set_a and set_b:", union_set)

# Set intersection
intersection_set = set_a & set_b
print("Intersection of set_a and set_b:", intersection_set)

# Set difference
difference_set = set_a - set_b
print("Difference of set_a and set_b:", difference_set)

# Set symmetric difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)