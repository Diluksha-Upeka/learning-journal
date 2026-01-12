# O(1)
# Constant Time Complexity
# Following operations are examples of O(1) time complexity:

# Arrays
numbers = [10, 20, 30, 40, 50]
numbers.append(60)  # Adding an element to the end of the array
numbers.pop()        # Removing the last element from the array
numbers[2]        # Accessing the third element in the array

# Dictionaries
person = {}
person['name'] = 'Alice'  # Adding a key-value pair
print(person['name'])    # Accessing a value by key
del person['name']       # Removing a key-value pair
person.pop('age', None)  # Removing a key-value pair with default
person.get('name')       # Accessing a value by key with default

# O(n)
# Linear Time Complexity
# Following operations are examples of O(n) time complexity:

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)  # Iterating through the array and printing each element

sum_numbers = 0
for num in numbers:
    sum_numbers += num  # Calculating the sum of all elements in the array
print(sum_numbers)

numbers.insert(0, 5)  # Inserting an element at the beginning of the array
numbers.remove(30)    # Removing a specific element from the array
print(10 in numbers)  # Checking if an element exists in the array

# O(log n)
# Logarithmic Time Complexity
# Following operations are examples of O(log n) time complexity:

# Binary search on a sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = binary_search(sorted_numbers, 70)  # O(log n) - divides search space in half each time

# O(n log n)
# Linearithmic Time Complexity
# Following operations are examples of O(n log n) time complexity:

numbers = [64, 34, 25, 12, 22, 11, 90]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_numbers = merge_sort(numbers)  # O(n log n) - efficient sorting algorithm

# Built-in sort (also O(n log n))
numbers.sort()  # Python's Timsort algorithm
sorted_list = sorted(numbers)  # Also O(n log n)

# O(n²)
# Quadratic Time Complexity
# Following operations are examples of O(n²) time complexity:

numbers = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

bubble_sort(numbers.copy())  # O(n²) - nested loops through the array

# Nested loops to find all pairs
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(f"Pair: ({numbers[i]}, {numbers[j]})")  # O(n²)

# Finding duplicates with nested loops
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


# SUMMARY OF TIME COMPLEXITIES (from fastest to slowest):
# O(1)       - Constant: Array access, hash table operations
# O(log n)   - Logarithmic: Binary search, balanced tree operations
# O(n)       - Linear: Simple loops, linear search
# O(n log n) - LinearLogarithmic: Efficient sorting (merge sort, quicksort)
# O(n²)      - Quadratic: Nested loops, bubble sort

# SPACE COMPLEXITY NOTES:
# Space complexity measures the amount of memory an algorithm uses
# - O(1): Constant space - only uses fixed amount of variables
# - O(n): Linear space - uses space proportional to input size (e.g., creating a copy)
# - O(log n): Logarithmic space - recursive calls in binary search
# - O(n²): Quadratic space - 2D arrays or matrices

