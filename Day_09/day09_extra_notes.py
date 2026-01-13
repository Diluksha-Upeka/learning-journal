# Arrays are stored in contiguous memory locations.
# Creating a new list = allocating new memory.

# Opposite Direction Two Pointers
# left-> <- right
# Used when,
    # Reversing a list/array
    # Checking for palindrome
    # Pair sum problems (like 2 sum, 3 sum, etc.)
    # Removing duplicates from sorted array
    # Move zeros to end

while left < right:
    swap() # arr[ left ], arr[ right ] = arr[ right ], arr[ left ]
    left += 1
    right -= 1

# Same direction Two Pointers (Fast and Slow pointers)
#  slow -> fast ->
#  Used when,
    # Removing duplicates from sorted array
    # Removing zeros
    # filtering in-place


# Sliding Window Technique (Dynamic 2 Pointers))
#  left -> [window] <- right
# Used when,
    # Subarray sums
    # Longest substring
    # Maximum window problems

# What happens if the array has 0 or 1 element?
    # loop will not run - safe edge case