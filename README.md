#Siris Neupane
Sales Tax Calculator

Project Overview
This project includes a Python module that calculates the total amount to charge a customer at checkout, including sales tax, based on the state (Montana, Idaho, Washington) and the type of items purchased. The types of items supported are "Wic Eligible food", "Software", and "everything else". The module is designed to not process refunds and adheres to the specific tax rules of each state:

Montana (MT): No sales tax.
Idaho (ID): 6% sales tax, except on software which is tax-exempt.
Washington (WA): 9.38% sales tax, inclusive of the average local tax.

Repository Contents
total_calculator.py: Contains the calculate_total function and the Item data class.
test_total_calculator.py: Includes unit tests for the calculate_total function using Python's unittest framework.
README.md: Provides an overview and instructions on how to run the tests.

Setup and Running Tests
To run the tests for this project, you will need Python installed on your system. It is recommended to use Python 3.8 or higher. You can run the tests directly from the command line:

Clone the repository:

git clone <repository-url>
cd <repository-directory>
Run the tests:

python -m unittest test_total_calculator.py

OR
you can run it from pycharm or any python IDE

Functionality
The calculate_total function takes two arguments:

state_code (str): A two-character abbreviation for the state ('MT', 'ID', 'WA').
items (list of Item): A list of Item instances to be purchased. Each Item includes a name, price, and type.
This function computes the total price including applicable taxes based on the state and item types. The tax rules are as described above, with specific exemptions for certain item types in each state.

Academic Deliverables
Production and Test Code: Both are located in this repository.
Documentation: This README provides a summary of the project and instructions for running the tests.
Additional Notes
Ensure that all dependencies and Python versions are correctly set up and compatible.
If you encounter any issues with running the tests, consider verifying your Python environment and dependencies.
