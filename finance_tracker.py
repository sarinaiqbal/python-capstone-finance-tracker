'''
Author: Sarina Iqbal
Python Capstone Project: Personal Finance Tracker
Description: This program makes use of core Python concepts to build
a simple command-line personal finance tracker that allows users 
to log expenses, categorize them, and view summaries.
'''

print("Welcome to the Personal Finance Tracker!")

# Function defining menu logic
def menu():
    while True: # Loop to repeatedly ask users for options
        print("What would you like to do?")
        print('''
        1. Add Expense
        2. View All Expenses
        3. View Summary
        4. Exit
        ''')
        option = int(input("Choose an option: "))

        if option == 1:
            add()
        elif option==2:
            view_expenses(data)
        
        elif option==3:
            view_summary(data)
        
        elif option==4:
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number from 1- 4")

data = {} # Dictionary to hold the expenses with details

''' This function asks user input for expenses with a description, category, and amount.
    It stores the data in the (global) dictionary named data with category as key and list 
    of tuples containing description and amount as values. It uses try-except blocks to handle
    invalid/empty inputs and unexpected errors gracefully.
'''
def add():
    try:
        expense = input("Enter expense description: ").strip() # strip any unnecessary whitespace
        # Handle empty inputs
        if expense == None or expense == "":
            raise ValueError("Description cannot be empty.")
        
        category = input("Enter category: ").strip() # strip any unnecessary whitespace
        # Handle empty inputs
        if category == None or category == "":
            raise ValueError("Category cannot be empty.")
        
        amount = float(input("Enter amount: "))
        # Restrict amounts less than 0
        if amount<=0 :
            raise ValueError("Amount must be greater than 0.")
        
    except ValueError as ve:
        print(f"Invalid input. {ve}")
    
    else: # If no errors, add expense data to dictionary
        tup = (expense, amount)  # Make tuple with expense description and amount
        # If input category is new, make new key in dictionary
        if category not in data: 
            data[category] = []
        data[category].append(tup) # If category already exists, append the details to it 
        print("Expense added successfully.")#Print success message
    
''' This function prints all categories and their expenses. The parameter is
    data, which is the dictionary that holds the expenses with details.'''
def view_expenses(data):
    # If expense dictionary is empty, print a message
    if len(data)==0:
        print("No expenses have been added.")
    else:
        for key, val in data.items(): # Iterating into dictionary
            print("Category: " + key)
            for i in val: # Iterating into list of tuples with description and amount
                print(f"  - {i[0]}: ${i[1]}") # print in the format: "- Description : $Amount"

''' This function shows the total amount spent per category. The parameter is 
    data, which is the dictionary that holds the expenses with details.'''
def view_summary(data):
    # If expense dictionary is empty, print a message
    if len(data)==0:
        print("No expenses have been added.")
    else:
        print("Summary: ")
        for key, val in data.items(): # Iterating into dictionary
            cat_sum = 0 # Initializing the sum for each category
            print() # Print blank line
            for i in val: # Iterating into list of tuples with description and amount
                cat_sum += i[1] # Adding up the amounts under each category
            # print in the format: "Category: sum(rounded to 2 decimal places)
            print(f"{key}: ${cat_sum:.2f}")


menu() # Call the function with the menu logic to start program
