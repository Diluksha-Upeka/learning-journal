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

