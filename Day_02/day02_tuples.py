# TUPLES
# A tuple is an immutable ordered collection of items. (can't be changed after creation)

import sys
import timeit

modules_1 = ['a', 'b', 'c', 'd', 'e']
modules_2 = modules_1  # Both variables point to the same list
print(modules_1)
print(modules_2)

tuple_1 = ('a', 'b', 'c', 'd', 'e')
tuple_2 = tuple_1  # Both variables point to the same tuple
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'z'  # This will raise an error because tuples are immutable

# NO methods like append, insert, remove, pop, sort, reverse for tuples

# Size comparison
print(sys.getsizeof(modules_1))  # Size of modules_1 in bytes - list has more overhead (104)
print(sys.getsizeof(tuple_1))  # Size of tuple_1 in bytes - tuple has less overhead (80)

# Speed comparison
lists_time =timeit.timeit(stmt = "modules = ['a', 'b', 'c', 'd', 'e']", number = 1000000)
tuples_time = timeit.timeit(stmt = "tuples = ('a', 'b', 'c', 'd', 'e')", number = 1000000)

if lists_time < tuples_time:
    print(f"Lists are faster: {lists_time} seconds")
else:
    print(f"Tuples are faster: {tuples_time} seconds")


# SETS - Unordered collection of unique elements with no duplicates
cs_courses = {'DSA', 'Python', 'Web Development', 'Python'}  # 'Python' will be stored only once
print(cs_courses)

# membership test - sets are optimized for this
print('DSA' in cs_courses)  # True
print('Machine Learning' in cs_courses)  # False

bio_courses = {'Biology', 'Chemistry', 'Physics', 'DSA', 'Python'}
# set operations
print(cs_courses.intersection(bio_courses))  # common elements
print(cs_courses.union(bio_courses))  # all unique elements
print(cs_courses.difference(bio_courses))  # elements in cs_courses but not in bio_courses
print(bio_courses.difference(cs_courses))  # elements in bio_courses but not in cs

# Empty list, tuple, set
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # This creates an empty dictionary, not a set
empty_set = set()
