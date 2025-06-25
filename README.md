# Personal Finance Tracker

## Overview
The Python Personal Finance Tracker is a simple command-line application that allows users to track daily expenses. The user is able to add expenses bearing a description, category, and numerical amount. Once added, the user can choose to view the expenses grouped by category and a summary of the total expenditure per category. The data is stored and retained only for a single session. 

## How to run the script:
1. Ensure Python is installed in your system. 
2. Save the script/code to a .py file, for example, `finance_tracker.py`
3. Run the code from your terminal or command prompt with the command:
   ```bash
   python finance_tracker.py
   ```
5. Follow the on-screen menu and enter your chosen options

## Python Concepts Used:
1. Functions: The program is organized into four different functions, namely `menu()`, `add()`, `view_expenses()` and `view_summary()`, that help break down the code into reusable blocks and prevent unnecessary code repetitions.
2. Data types: 
  - `String`: Strings are used to collect user inputs, print messages and texts, and `String` methods such as `strip()` are also used for appropriate input processing. 
  - `int`: ints are used when 
  - `float`: - floats are used to handle expense amount inputs and in the calculation of expense summaries. 
3. Data Structures: 
  - Dictionaries: The dictionary `data` is used to store the expense inputs as key value pairs, with the category being the key and a list of values (description and amount). 
  - Lists: The dictionary values are lists bearing the tuples that contain the expense descriptions and amounts.
  - Tuples - The expense descriptions and amounts are stored into tuples, ensuring the details are unchanged once created. 
4. Exception handling - `try/except` blocks and `raise` statements help the program run smoothly by handling exceptions and preventing unexpected errors from occurring. 
5. Conditional (`if/else`) statements: Allow smooth decision making by defining menu logic and validating user inputs. 
6. Loops: `while` loops allow repetition of tasks including repeatedly asking the user for their expenses inputs; `for` loops allow iteration over dictionaries and lists. 
