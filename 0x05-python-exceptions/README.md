* 0x05. Python - Exceptions
Project Description
This project involves working with Python and exceptions. You will need to implement functions that handle various exceptions, print information about objects, and work with Python lists, bytes, and floats.

Project Details
Author: Guillaume
Weight: 1
Start Date: October 23, 2023, 6:00 AM
End Date: October 24, 2023, 6:00 AM
Checker Release Date: October 23, 2023, 12:00 PM
Auto Review: An auto review will be launched at the deadline
Resources
You should read or watch the following resources to understand exceptions in Python:

Errors and Exceptions
Learn to Program 11 Static & Exception Handling (starting at minute 7)
Learning Objectives
By the end of this project, you should be able to explain the following concepts without needing to use Google:

** General:

Why Python programming is awesome
The difference between errors and exceptions
What exceptions are and how to use them
When to use exceptions
How to correctly handle an exception
The purpose of catching exceptions
How to raise a built-in exception
When to implement a clean-up action after an exception
Copyright - Plagiarism
You are responsible for solving the tasks below on your own. Plagiarism is strictly forbidden, and any form of it will result in removal from the program. You are not allowed to publish any content of this project.

** Requirements
** General:

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
Tasks
** 0. Safe list printing (mandatory)
Implement a function that prints a specified number of elements from a list, using exception handling.

Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print.
x can be bigger than the length of my_list.
Returns the real number of elements printed.
You have to use try: / except:.
You are not allowed to import any module.
You are not allowed to use len().
** 1. Safe printing of an integers list (mandatory)
Write a function that prints an integer using the "{:d}".format() format.

Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.).
The integer should be printed followed by a new line.
Returns True if value has been correctly printed (it means the value is an integer).
Otherwise, returns False.
You have to use try: / except:.
You have to use "{:d}".format() to print as an integer.
You are not allowed to import any module.
You are not allowed to use type().
** 2. Print and count integers (mandatory)
Implement a function that prints the first x elements of a list and only integers, using exception handling.

Prototype: def safe_print_list_integers(my_list=[], x=0):
my_list can contain any type (integer, string, etc.).
All integers have to be printed on the same line followed by a new line, other types of values in the list must be skipped.
x represents the number of elements to access in my_list.
x can be bigger than the length of my_list. If it's the case, an exception is expected to occur.
Returns the real number of integers printed.
You have to use try: / except:.
You have to use "{:d}".format() to print an integer.
You are not allowed to import any module.
You are not allowed to use len().
** 3. Integers division with debug (mandatory)
Write a function that divides two integers and prints the result, using exception handling.

Prototype: def safe_print_division(a, b):
You can assume that a and b are integers.
The result of the division should print on the finally: section, preceded by "Inside result:".
Returns the value of the division; otherwise, returns None.
You have to use try: / except: / finally:.
You have to use "{}".format() to print the result.
You are not allowed to import any module.
** 4. Divide a list (mandatory)
Write a function that divides element by element two lists and handles exceptions, using exception handling.

Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.).
list_length can be bigger than the length of both lists.
Returns a new list (length = list_length) with all divisions.
If two elements can't be divided, the division result should be equal to 0.
If an element is not an integer or float, print "wrong type".
If the division can't be done (dividing by 0), print "division by 0".
If my_list_1 or my_list_2 is too short, print "out of range".
You have to use try: / except: / finally:.
You are not allowed to import any module.
** 5. Raise exception (mandatory)
Write a function that raises a type exception.

Prototype: def raise_exception():
You are not allowed to import any module.
** 6. Raise a message (mandatory)
Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):
You are not allowed to import any module.
** 7. Safe integer print with error message (advanced)
Implement a function that prints an integer and handles errors, printing an error message in stderr, using exception handling.

Prototype: def safe_print_integer_err(value):
value can be any type (integer, string, etc.).
The integer should be printed followed by a new line.
Returns True if value has been correctly printed (it means the value is an integer).
Otherwise, returns False and prints in stderr the error precede by "Exception: ".
You have to use try: / except:.
You have to use "{:d}".format() to print as an integer.
You are not allowed to import any module.
You are not allowed to use type().
** 8. Safe function (advanced)
Write a function that executes a function safely.

Prototype: def safe_function(fct, *args):
You have to use try: / except:.
The *args can contain any type.
The function should return None if the function can't be executed, and print (in stderr) the exception class and the message (use a space to separate exception message and class).
** 9. ByteCode -> Python #4 (advanced)
Please download the provided zip file and write a function that displays the program's bytecode.

Prototype: def magic_calculation(a, b):
Returns the sum of a and b.
You have to use the dis module to print the bytecode of your function.
Your code should not be executed when imported.
