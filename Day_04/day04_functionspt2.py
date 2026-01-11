# Number of days in each month; index 0 is a placeholder for easier indexing
month_days =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    """Returns True if year is a leap year, False otherwise."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
    """Returns the number of days in the given month and year."""
    if month < 1 or month > 12:
        return "Invalid Month"
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]

# Example usage:
print(is_leap_year(2020))  # True

print(days_in_month(2020, 2))  # 29
print(days_in_month(2021, 2))  # 28


# ARGS AND KWARGS EXPLANATION
# *args and **kwargs allow you to pass a variable number of arguments to a function.
# *args is used to pass a variable number of non-keyword arguments (positional arguments) to a function.
# **kwargs is used to pass a variable number of keyword arguments (named arguments) to a function.

# postional arguments
# def add(a, b):
#     return a + b

# named arguments
# def introduce(name, age):
#     return f"Hi, my name is {name} and I'm {age} years old."