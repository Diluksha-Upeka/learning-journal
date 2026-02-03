# Messy Code Example

import json, os


def calculate(x, y):
    result = x + y
    print("The sum is", result)
    return result


data = [1, 2, 3, 4, 5]
for i in data:
    print(calculate(i, i * 2))
