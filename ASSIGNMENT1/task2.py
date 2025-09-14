'''
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:

Enter first name and last name: John
Enter first name and last name: Doe

Hello, John Doe! Welcome to the Python program.
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(f"\nHello, {full_name}! Welcome to the Python world")