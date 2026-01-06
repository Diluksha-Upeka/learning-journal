# DICTIONARY VS LIST SPEED TESTING

import time

# Create a large list and a large dictionary
large_list = list(range(1000000))
large_dict = {str(i): i for i in range(1000000)}

target_index = 999999 # Last element in the list and dictionary

# Test the speed of accessing elements in the list
start_time = time.time()
if target_index in large_list:
    print(f"Found {target_index} in list")
end_time = time.time()

print(f"List access time: {end_time - start_time} seconds")

# Test the speed of accessing elements in the dictionary
start_time = time.time()
if str(target_index) in large_dict:
    print(f"Found {target_index} in dictionary")
end_time = time.time()

print(f"Dictionary access time: {end_time - start_time} seconds")


# List access time: 0.00801229476928711 seconds
# Dictionary access time: 0.0 seconds
# As observed, dictionary access is significantly faster than list access for large datasets.

