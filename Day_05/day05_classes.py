# OOP - Object-Oriented Programming
# Class - blueprint
# Object - instance

class Employee:
    def __init__(self, first = "", last = "", pay = 0): # constructor method
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay
    
    def fullname(self):             # method should have self parameter
        return '{} {}'.format(self.first, self.last)

# Instantiating a class
# Data unique to each object

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

# Setting attributes after instantiation
# emp_1.first = "John"
# emp_1.last = "Doe"
# emp_1.email = "jdoe@ex.com"
# emp_1.pay = 50000

# emp_2.first = "Jane"
# emp_2.last = "Smith"
# emp_2.email = "jsmith@ex.com"
# emp_2.pay = 60000

print(emp_1.email) # accessing attributes
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.pay))

print(emp_1.fullname()) # parentheses to call method
print(emp_2.fullname())

# Alternative way to call method
Employee.fullname(emp_1) # calling method using class name and passing instance
Employee.fullname(emp_2)
