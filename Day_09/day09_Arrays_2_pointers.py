# ARRAYS 2 POINTERS (List Reversal)

# Reverse an array using 2 pointers
def reverse_array(arr):
    # 2 pointers starts at the beginning and end of the array
    left = 0
    right = len(arr) - 1

    # Swap elements until the pointers meet in the middle
    while left < right:
        # swap the values
        # arr[left], arr[right] = arr[right], arr[left]
        # Using a temporary variable to swap
        # Above line can also be used instead of below 3 lines
        temp = arr[left]
        arr[left] = arr[right]  
        arr[right] = temp

        # Move the pointers closer to the middle
        left += 1
        right -= 1
    return arr

print(reverse_array([1, 2, 3, 4, 5]))

# If I use new_list = reverse_array([1, 2, 3, 4, 5])
# Then new_list will be [5, 4, 3, 2, 1] But the original list [1, 2, 3, 4, 5] will be changed to [5, 4, 3, 2, 1] as well

#If I use new_list = old_list[::-1]
# Then new_list will be [5, 4, 3, 2, 1]
# Extra space will be used for new_list but the original list old_list will remain unchanged
# Space Complexity: O(n)
# Time Complexity: O(n)

# Using 2 pointers is more efficient than using extra space
# Space Complexity: O(1)
# Time Complexity: O(n)