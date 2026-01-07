# FUNCTIONS

def hello():
    print("Hello, function!") 

# hello()  # Call the function to print the message

# DRY PRINCIPLE - Don't Repeat Yourself

def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Alice'))

def hello_func(greetings, name ='You'):
    return '{}, {}'.format(greetings, name)

print(hello_func('Hello', name ='John'))

# ARGS AND KWARGS

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# args - positional arguments
student_info('Math', 'Art', name='Alice', age=22)

# args as tuple and kwargs as dict

# kwargs - keyword arguments
student_info(name='Bob', age=25)

courses = ['Math', 'Science', 'Art']
info = {'name': 'Charlie', 'age': 23}
student_info(*courses, **info)

# ARGS VS KWARGS

# Without args and kwargs
    # Not flexible, fixed number of parameters
    # Not suitable for rapid development

# *args
    # Flexible number of positional arguments
    # values
    # Tuple data type - ordered, indexed, immutable
    # Use when number of inputs is unknown

# **kwargs
    # Flexible number of keyword arguments
    # key-value pairs
    # Dictionary data type - unordered, key-value pairs, mutable