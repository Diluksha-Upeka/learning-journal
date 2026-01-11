# Lists
# A list is a mutable ordered collection of items. (can be changed after creation)

modules = ['Control systems', 'DSA', 'Python', 'Web Development']

print(modules)
# Accessing elements
print(modules[0])  # First element
print(modules[-1])  # Last element

# adding elements
modules.append('Machine Learning')
print(modules)

modules.insert(2, 'Data Science')
print(modules)

# slicing
print(modules[1:4])  # Elements from index 1 to 3
print(modules[:3])   # First three elements
print(modules[2:])   # From index 2 to the end

# Extending lists
modules_2 = ['Cybersecurity', 'Cloud Computing']
modules.extend(modules_2)
print(modules)
print(modules[-1])  # Last element after extending

# Removing elements
# modules.remove('DSA')
# print(modules)

popped_module = modules.pop()  # Removes last element
print(popped_module)
print(modules)

#sorting
# modules.reverse()
# print(modules)

modules.sort() # Sorts the list in place in ascending order
print(modules)

nums = [5, 2, 9, 1, 5, 6]
nums.sort()  # for descending order use nums.sort(reverse=True)
print(nums)

# When you don't want to modify the original list use sorted()
sorted_modules = sorted(modules)  # returns a new sorted list
print(sorted_modules)

# Min, Max, Sum of a list
print(min(nums)) 
print(max(nums))
print(sum(nums))

# Finding the index of an element .index() and checking membership with 'in'
print(modules.index('DSA'))
print('DSA' in modules)  # Check if 'DSA' is in the list

# Iterating through a list using for loop
for index, item in enumerate(modules, start=1):  # enumerate returns a tuple of index and value for each item in the modules:
    # number and item
    print(index,item) 

module_str = ' -  '.join(modules)  # Joining list elements into a string
print(module_str)

new_list = module_str.split(' -  ')  # Splitting string back into a list
print(new_list)