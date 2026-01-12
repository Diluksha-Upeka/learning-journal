# COMMON SEARCHING ALGORITHMS 

# 1. LINEAR SEARCH (Sequential Search)

# Description: Iterates through each element sequentially until target is found
# Time Complexity: O(n) - worst case checks every element
# Space Complexity: O(1) - only uses constant extra space
# When to use: Unsorted data, small datasets, or when simplicity is priority
# Pros: Simple to implement, works on unsorted data
# Cons: Inefficient for large datasets

# 2. BINARY SEARCH

# Description: Divides sorted array in half repeatedly, comparing middle element
# Time Complexity: O(log n) - eliminates half the search space each iteration
# Space Complexity: O(1) iterative, O(log n) recursive (call stack)
# When to use: Sorted arrays or when you can sort first
# Pros: Very efficient for large sorted datasets
# Cons: Requires sorted data, more complex than linear search
# Key Points:
#   - MUST have sorted data
#   - Classic divide-and-conquer algorithm
#   - Most asked searching algorithm in interviews


# COMMON SORTING ALGORITHMS 


# 1. BUBBLE SORT

# Description: Repeatedly swaps adjacent elements if they're in wrong order
# Time Complexity: O(n²) average/worst, O(n) best case (already sorted)
# Space Complexity: O(1) - in-place sorting
# Stable: Yes (maintains relative order of equal elements)
# When to use: Teaching purposes, nearly sorted small datasets
# Pros: Simple to understand and implement, stable
# Cons: Very inefficient for large datasets
# Interview Notes: Know it exists, but mention it's inefficient

# 2. SELECTION SORT

# Description: Finds minimum element and places it at beginning, repeat
# Time Complexity: O(n²) in all cases
# Space Complexity: O(1) - in-place sorting
# Stable: No (default implementation)
# When to use: Small datasets, when memory write is costly
# Pros: Simple, minimal number of swaps (n-1 swaps)
# Cons: Inefficient for large datasets, not stable
# Interview Notes: Better than bubble sort in practice due to fewer swaps

# 3. INSERTION SORT

# Description: Builds sorted array one element at a time by inserting elements
# Time Complexity: O(n²) average/worst, O(n) best case (already sorted)
# Space Complexity: O(1) - in-place sorting
# Stable: Yes
# When to use: Small datasets, nearly sorted data, online sorting
# Pros: Simple, efficient for small/nearly sorted data, stable, adaptive
# Cons: Inefficient for large unsorted datasets
# Interview Notes: Good for small datasets or as part of hybrid algorithms

# 4. MERGE SORT  (VERY IMPORTANT FOR INTERVIEWS)

# Description: Divide array in half, recursively sort, then merge sorted halves
# Time Complexity: O(n log n) in all cases (best, average, worst)
# Space Complexity: O(n) - requires additional space for merging
# Stable: Yes
# When to use: Large datasets, when stability needed, linked lists
# Pros: Guaranteed O(n log n), stable, predictable performance
# Cons: Requires extra space, slower than quicksort in practice
# Interview Notes: 
#   - Go-to algorithm for guaranteed O(n log n)
#   - Divide-and-conquer paradigm
#   - Preferred for linked lists
#   - Used in external sorting

# 5. QUICK SORT  (VERY IMPORTANT FOR INTERVIEWS)

# Description: Pick pivot, partition around it, recursively sort partitions
# Time Complexity: O(n log n) average, O(n²) worst case (bad pivot choice)
# Space Complexity: O(log n) for recursive call stack
# Stable: No (default implementation)
# When to use: General purpose sorting, large datasets
# Pros: Fast in practice, in-place, cache-friendly
# Cons: Unstable, worst case O(n²), not good for nearly sorted data
# Interview Notes:
#   - Most commonly used sorting algorithm in practice
#   - Pivot selection strategies: first, last, median, random
#   - Can be optimized with 3-way partitioning for duplicates
#   - Used in many language libraries (with optimizations)

# 6. HEAP SORT

# Description: Build max heap, repeatedly extract maximum to sorted array
# Time Complexity: O(n log n) in all cases
# Space Complexity: O(1) - in-place sorting
# Stable: No
# When to use: When O(n log n) guaranteed and O(1) space needed
# Pros: Guaranteed O(n log n), in-place, no worst case like quicksort
# Cons: Not stable, slower than quicksort in practice, not cache-friendly
# Interview Notes: Good for priority queue implementations


# QUICK COMPARISON TABLE - MOST ASKED IN INTERVIEWS


# Algorithm          | Time (Best)  | Time (Avg)   | Time (Worst) | Space   | Stable
# -------------------------------------------------------------------------------
# Bubble Sort        | O(n)         | O(n²)        | O(n²)        | O(1)    | Yes
# Selection Sort     | O(n²)        | O(n²)        | O(n²)        | O(1)    | No
# Insertion Sort     | O(n)         | O(n²)        | O(n²)        | O(1)    | Yes
# Merge Sort ⭐      | O(n log n)   | O(n log n)   | O(n log n)   | O(n)    | Yes
# Quick Sort ⭐      | O(n log n)   | O(n log n)   | O(n²)        | O(log n)| No
# Heap Sort          | O(n log n)   | O(n log n)   | O(n log n)   | O(1)    | No


# KEY INTERVIEW POINTS TO REMEMBER


# SORTING:
# 1. Know the difference between stable and unstable sorts
# 2. Understand when to use O(n²) vs O(n log n) algorithms
# 3. Merge Sort: guaranteed O(n log n), needs extra space, stable
# 4. Quick Sort: fastest in practice but O(n²) worst case, in-place
# 5. Heap Sort: guaranteed O(n log n) and in-place, but not stable
# 6. For nearly sorted data: Insertion Sort is O(n)
# 7. For small datasets (n < 10-20): Insertion Sort often fastest
# 8. Non-comparison sorts (Counting, Radix, Bucket) can beat O(n log n)

# SEARCHING:
# 1. Binary Search is the MOST important - know it cold
# 2. Always check if data is sorted before using binary search
# 3. For unsorted data: Linear Search is your only option (or sort first)
# 4. Binary Search variations: find first/last occurrence, rotation point
# 5. For range queries: Binary Search to find start and end positions

# WHEN ASKED "WHICH ALGORITHM TO USE":
# - Small dataset (< 50 elements): Insertion Sort
# - Need guaranteed O(n log n): Merge Sort or Heap Sort
# - General purpose, fast: Quick Sort (with random pivot)
# - Need stability: Merge Sort or Tim Sort
# - Limited space: Heap Sort or Quick Sort
# - Known integer range: Counting Sort or Radix Sort
# - Mostly sorted data: Insertion Sort or Tim Sort
# - Searching sorted data: Binary Search
# - Searching unsorted data: Linear Search (or sort first)

# COMMON INTERVIEW VARIATIONS:
# - Sort colors (Dutch National Flag): 3-way partition
# - Find kth largest/smallest: Quick Select O(n) average
# - Merge k sorted arrays: Min heap approach
# - Sort linked list: Merge Sort (O(1) space for linked lists)
# - Find element in rotated sorted array: Modified Binary Search
# - Search in 2D matrix: Treat as 1D array + Binary Search