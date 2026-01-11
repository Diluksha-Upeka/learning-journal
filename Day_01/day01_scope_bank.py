# LEGB - Local, Enclosing, Global, Built-in

bank_balance = 1000  # Global variable

#bad practice to use global variables
def hack_the_bank():
    global bank_balance  # Declare that we want to use the global variable
    bank_balance = 0  # Modify the global variable
    print(f"Hacked! New bank balance is: {bank_balance}")

#Good practice to avoid using global variables unless necessary
def secure_transaction(current_balance, amount):
    #'current_balance' is a local variable
    new_balance = current_balance - amount  # 'new_balance' is also a local variable
    if new_balance < 0:
        print("Transaction declined: Insufficient funds.")
        return current_balance
    else:
        print(f"Transaction approved! New balance is: {new_balance}")
        return new_balance
    
# Testing the functions
print(f"Initial bank balance: {bank_balance}")

# # Attempt to hack the bank
# hack_the_bank()
# print(f"Bank balance after hack attempt: {bank_balance}")
# Perform a secure transaction
bank_balance = secure_transaction(bank_balance, 200)
print(f"Final bank balance: {bank_balance}")


#Why global variables are bad practice in a large codebase?
# 1. They can be modified from anywhere in the code, making it hard to track
#    changes and debug issues.
# 2. They can lead to unintended side effects if different parts of the code
#    modify the same global variable.
# 3. They make the code less modular and harder to test, as functions
#    depend on external state.


#enclosing scope example
def outer_function():
    outer_var = "I'm from the outer function" 

    def inner_function():
        inner_var = "I'm from the inner function"
        print(inner_var)  # Local scope 
        print(outer_var)  # Enclosing scope

    inner_function()

outer_function()
