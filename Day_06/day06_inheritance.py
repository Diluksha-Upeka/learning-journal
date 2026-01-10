# INHERITANCE IN PYTHON

# Base class
class Employee:

    raise_amount = 1.05
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

# Derived class
class Developer(Employee):
    raise_amount = 1.10  # Overriding the raise amount for developers
    # Additional methods or attributes specific to Developer can be added here
    # Raise amount is overridden to 10% for developers

    def __init__(self, first, last, salary, prog_lang=None):
        super().__init__(first, last, salary) # Call the constructor of the base class
        # Employee.__init__(self, first, last, salary) - DRY principle
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.full_name())

dev_1 = Developer("John", "Doe", 80000) 
dev_2 = Developer("Jane", "Smith", 90000)
dev_3 = Developer("Alice", "Johnson", 95000, prog_lang="Python")

print(dev_1.salary)  # Output: 80000
dev_1.apply_raise()
print(dev_1.salary)  # Output: 88000 (80000 * 1.10)

# print(help(Developer))  # Displays the method resolution order and inheritance details

print(dev_1.full_name())  # Output: John Doe
print(dev_2.full_name())  # Output: Jane Smith
print(dev_3.prog_lang)  # Output: Python

mgr_1 = Manager("Sara", "Connor", 120000, [dev_1])
print(mgr_1.full_name())  # Output: Sara Connor

mgr_1.print_employees()  # Output: --> John Doe
mgr_1.add_employee(dev_2)
mgr_1.print_employees()  # Output: --> John Doe --> Jane Smith
mgr_1.remove_employee(dev_1)
mgr_1.print_employees()  # Output: --> Jane Smith

# print(isinstance(mgr_1, Manager))  # True
# print(isinstance(mgr_1, Employee))  # True
# print(isinstance(mgr_1, Developer))  # False

# print(issubclass(Manager, Employee))  # True
# print(issubclass(Developer, Employee))  # True    
# print(issubclass(Manager, Developer))  # False