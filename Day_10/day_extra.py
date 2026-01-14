# Hash maps collision handling using Separate Chaining
# When collision happens, we store multiple key-value pairs in the same bucket using a list

# Each bucket is like a room with a bunk bed (list) to hold multiple items
# Time Complexity: O(1) on average for add and get operations, but can degrade to O(n) in worst case if many collisions occur

# For avoiding collisions, we can:
# 1. Use a better hash function that distributes keys more uniformly
# 2. Increase the size of the hash map to reduce the load factor
# 3. Use a different data structure (e.g., a linked list) to handle collisions

# Space Complexity: O(n)
# Time Complexity: O(1)

