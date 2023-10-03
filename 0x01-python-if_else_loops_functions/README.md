# Project: Python - if/else, loops, functions
## Overview
This project consists of a series of Python tasks designed to help you practice and improve your skills in using if/else statements, loops, and functions in Python. The tasks range from simple conditional statements to more complex problems involving loops and functions.

## Project Details
* Learning Objectives
* By completing this project, you are expected to achieve the following learning objectives:

* Understand why Python programming is valuable and important.
* Recognize the significance of proper indentation in Python code.
* Learn to use if and if...else statements effectively.
* Gain proficiency in adding comments to your code.
* Learn to assign values to variables and manipulate them.
* Understand the usage of while and for loops in $  Python.
* Differentiate Python's "for" loop from C's.
* Learn how to use break and continue statements in loops.
* Master the use of else clauses with loops.
* Understand the purpose of the "pass" statement and when to use it.
* Learn how to utilize the "range" function.
* Comprehend the concept of functions and how to define and use them.
* Understand the return statement in functions and how it works.
* Gain knowledge about the scope of variables.
* Learn what a traceback is in Python.
* Familiarize yourself with arithmetic operators and their usage.
## Requirements
* All Python scripts should be created using editors like vi, vim, or emacs.
* All Python files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5).
* All Python files should end with a new line.
* The first line of all Python files should be * exactly #!/usr/bin/python3.
* A README.md file must be included at the root of the project folder.
* Your code should adhere to the pycodestyle style guide (version 2.8.*).
* All Python files must be executable.
* The length of your files will be tested using the wc command.
* In the case of C scripts, they should be compiled on Ubuntu 20.04 LTS using GCC with the options -Wall -Werror -Wextra -pedantic -std=gnu89.
* C files should also end with a new line.
* Your code should follow the Betty style. It will be checked using betty-style.pl and betty-doc.pl.
* You are not allowed to use global variables in C.
* Each C file should contain no more than 5 functions.
* The prototypes of all your functions should be included in a header file called lists.h.
* Don't forget to push your header file.
* All header files should be include guarded.
## Tasks
* Task 0: Positive anything is better than negative nothing
* Write a Python program that assigns a random signed number to a variable number each time it is executed.
* Complete the source code to print whether the number stored in the variable number is positive, negative, or zero.
* The output should follow the format: "The number, followed by if the number is greater than 0: is positive, if the number is 0: is zero, if the number is less than 0: is negative" followed by a new line.
## Example output:
#!csharp
#!Copy code
#!-4 is negative
#!0 is zero
#!10 is positive
#!You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/0-positive_or_negative.py.
## Task 1: The last digit
* Write a Python program that assigns a random signed number to the variable number each time it is executed.
* Complete the source code to print the last digit of the number stored in the variable number.
* The output should follow the format: "Last digit of number is last_digit, followed by:
"and is greater than 5" if the last digit is greater than 5.
"and is 0" if the last digit is 0.
"and is less than 6 and not 0" if the last digit is less than 6 and not 0.
## Example output:
#!csharp
#!Copy code
#!Last digit of 4205 is 5 and is less than 6 and not 0
#!Last digit of -626 is -6 and is less than 6 and not 0
#!You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/1-last_digit.py.
## Task 2: I sometimes suffer from insomnia...
* Write a Python program that prints the ASCII alphabet in lowercase, without a new line between the characters.
* You can only use one print function with string format.
* You can only use one loop in your code.
* You are not allowed to store characters in a variable.
* You are not allowed to import any module.
* Example output:
* Copy code
* abcdefghijklmnopqrstuvwxyz
* You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/2-print_alphabet.py.
## Task 3: When I was having that alphabet soup...
* Write a Python program that prints the ASCII alphabet in lowercase, excluding the letters 'q' and 'e', without a new line between the characters.
* Print all the letters except 'q' and 'e'.
* You can only use one print function with string format.
* You can only use one loop in your code.
* You are not allowed to store characters in a variable.
* You are not allowed to import any module.
## Example output:
#!Copy code
#!abcdfghijklmnoprstuvwxyz
#!You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/3-print_alphabt.py.
## Task 4: Hexadecimal printing
* Write a Python program that prints all numbers from 0 to 98 in decimal and hexadecimal format, as shown below:
* python
* Copy code
* 0 = 0x0
* 1 = 0x1
* 2 = 0x2
...
* 97 = 0x61
* 98 = 0x62
* You can only use one print function with string format.
* You can only use one loop in your code.
* You are not allowed to store numbers or strings in a variable.
* You are not allowed to import any module.
* You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/4-print_hexa.py.
## Task 5: 00...99
* Write a Python program that prints numbers from 0 to 99.
* Numbers must be separated by , , followed by a space.
* Numbers should be printed in ascending order, with two digits.
* The last number should be followed by a new line.
* You can only use no more than 2 print functions with string format.
* You can only use one loop in your code.
* You are not allowed to store numbers or strings in a variable.
* You are not allowed to import any module.
# Example output:
* Copy code
#!00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, ..., 98, 99
* You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/5-print_comb2.py.
## Task 6: Inventing is a combination of brains and materials. The more brains you use, the less material you need.
* Write a Python program that prints all possible different combinations of two digits.
* The two digits must be separated by , , followed by a space.
* The combinations should be printed in ascending order.
* Use only the characters '0' through '9' to print the combinations.
* The last combination should be followed by a new line.
* You can only use no more than 3 print functions with string format.
* You can only use no more than 2 loops in your code.
* You are not allowed to import any module.
## Example output:
## Copy code
#!00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, ..., 98, 99
* You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/6-print_comb3.py.
#Task 7: islower
-Write a Python function def islower(c): that checks for lowercase character.
-Prototype: def islower(c):
-Returns True if c is lowercase.
-Returns False otherwise.
-You can assume c is a single ASCII character.
-The function should not use any built-in Python function.
-You are not allowed to import any module.
-You are not allowed to use str.upper() and str.isupper().
-You are not allowed to use any conditional statement (if, for, etc.)
-You are not allowed to use any loops (while, for, etc.)
-You are not allowed to create any variable other than c.
* Example:
* python
* Copy code
>>> islower('a')
True
>>> islower('A')
False
>>> islower('1')
False
-You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/7-islower.py.
-Task 8: To uppercase
-Write a Python function def uppercase(str): that converts a string to uppercase.
-Prototype: def uppercase(str):
-Returns the uppercase version of the string.
-You can assume str will be a string of one or more characters.
-The function should not use any built-in Python function.
-You are not allowed to import any module.
-You are not allowed to use any loops (while, for, etc.)
-You are not allowed to use any conditional statements (if, for, etc.)
-You are not allowed to create any variable other than new_string.
-You can only use the variable new_string once.
* Example:
* python
Copy code
>>> uppercase("hello")
'HELLO'
>>> uppercase("Holberton School 98 Battery street")
'HOLBERTON SCHOOL 98 BATTERY STREET'
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/8-uppercase.py.
Task 9: There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
Write a Python function def print_last_digit(number): that prints the last digit of a number.
Prototype: def print_last_digit(number):
Returns the value of the last digit.
You can assume number will be a positive integer.
The function should not use any built-in Python function.
You are not allowed to import any module.
You are not allowed to use any loops (while, for, etc.)
You are not allowed to use any conditional statements (if, for, etc.)
You can only use one print function with format.
Example:
python
Copy code
>>> print_last_digit(98)
8
>>> print_last_digit(0)
0
>>> print_last_digit(-1024)
4
* You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/9-print_last_digit.py.
* Task 10: a + b
* Write a Python function def add(a, b): that adds two integers and returns the result.
* Prototype: def add(a, b):
* Returns the value of a + b.
* You are not allowed to import any module.
You can only use the + and - operators.
You are not allowed to use built-in functions like sum or math.sqrt.
You are not allowed to use loops (for, while, etc.)
You are not allowed to use conditional statements (if, else, etc.)
You are not allowed to create global or static variables.
You can only use operators + and - a maximum of four times in your code.
Example:
python
Copy code
>>> add(1, 1)
2
>>> add(5, 3)
8
>>> add(-4, 7)
3
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/10-add.py.
Task 11: a ^ b
Write a Python function def pow(a, b): that computes a to the power of b and returns the value.
Prototype: def pow(a, b):
Returns the value of a ^ b.
You are not allowed to import any module.
You can only use the * operator and the recursion.
You are not allowed to use loops (for, while, etc.)
You are not allowed to use conditional statements (if, else, etc.)
If b is negative, the function should return None.
Example:
python
Copy code
>>> pow(2, 3)
8
>>> pow(10, 0)
1
>>> pow(-4, 5)
-1024
>>> pow(5, -2)
None
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/11-pow.py.
Task 12: Fizz Buzz
Write a Python function def fizzbuzz(): that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."
Prototype: def fizzbuzz():
Each printed value should be separated by a space.
You are not allowed to use the if, else, or ternary operators.
You can only use one print function.
You can only use one loop (while, for, etc.)
Example output:
Copy code
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ...
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/12-fizzbuzz.py.
Task 13: Insert in sorted linked list
Write a Python function def insert_node(head, data): that inserts a new Node with the integer data at the correct position in a sorted linked list (increasing order).
Prototype: def insert_node(head, data):
Returns the head of the new linked list.
You can assume that this linked list will always be sorted in non-decreasing order.
If the head of the linked list is None (empty list), it should be set to a new Node with the given data.
You are not allowed to modify the nodes of the linked list.
You can only define a maximum of two functions:
int __length__(head): Function that calculates the length of the linked list.
Node *insert_at_end(Node *head, int data): Function that inserts a node at the end of the linked list.
You are not allowed to use any loops (for, while, etc.) or recursion.
Example:
python
Copy code
>>> class Node:
...     def __init__(self, data):
...         self.data = data
...         self.next = None
...
>>> def print_list(head):
...     current = head
...     while current:
...         print(current.data, end=' ')
...         current = current.next
...     print()
...
>>> head = Node(1)
>>> insert_node(head, 2)
>>> print_list(head)
1 2
>>> insert_node(head, 0)
>>> print_list(head)
0 1 2
>>> insert_node(head, 3)
>>> print_list(head)
0 1 2 3
>>> insert_node(head, 0)
>>> print_list(head)
0 0 1 2 3
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/13-insert_number.c.
Task 14: Basic dictionary
Write a Python function def simple_delete(a_dictionary, key=""): that deletes a key in a dictionary.
Prototype: def simple_delete(a_dictionary, key=""):
Returns the modified dictionary without the key/value pair if the key exists.
If the key does not exist in the dictionary, the function should return the dictionary unchanged.
You are not allowed to use pop(), popitem(), or any other method that will modify the dictionary while iterating through it.
You are not allowed to use loops (for or while).
Example:
python
Copy code
>>> a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
>>> new_dict = simple_delete(a_dictionary, 'track')
>>> print(new_dict)
{'language': "C", 'number': 89}
>>> new_dict = simple_delete(a_dictionary, 'c_is_fun')
>>> print(new_dict)
{'language': "C", 'number': 89, 'track': "Low level"}
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/14-simple_delete.py.
Task 15: City or State?
Write a Python function def weight_average(my_list=[]): that returns the weighted average of all integers tuple (weight, score) in the list.
Prototype: def weight_average(my_list=[]):
Returns 0 if the list is empty.
You are not allowed to import any module.
You can assume that all the weights are positive integers and the list is not empty.
Example:
python
Copy code
>>> my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
>>> weight_average(my_list)
2.6666666666666665
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/100-weight_average.py.
Task 16: Delete by value
Write a Python function def delete_by_value(my_list, x): that deletes all nodes of a linked list containing a specific value.
Prototype: def delete_by_value(my_list, x):
Returns the head of the updated linked list.
You are not allowed to use any loops (for, while, etc.) or recursion.
You are not allowed to use remove() or any built-in mutable method.
You are not allowed to create new nodes or objects, or change the head pointer.
Example:
python
Copy code
{
    PyObject *p;

>>> class Node:
...     def __init__(self, data):
...         self.data = data
...         self.next = None
...
>>> def print_list(head):
...     current = head
...     while current:
...         print(current.data, end=' ')
...         current = current.next
...     print()
...
>>> head = Node(1)
>>> print_list(head)
1
>>> head = delete_by_value(head, 1)
>>> print_list(head)
>>> print(head)
None
>>> head = Node(2)
>>> head = Node(1)
>>> print_list(head)
1 2
>>> head = delete_by_value(head, 1)
>>> print_list(head)
2
}
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/101-delete_by_value.c.
Task 17: CPython #2: PyFloatObject
Write a C function double c_python_print(PyObject *p); that prints a Python PyFloatObject.
Prototype: double c_python_print(PyObject *p);
The function must return the value of the PyFloatObject.
You are not allowed to use the Python C API (PyFloat_Check).
Your function should not crash or have undefined behavior if the object passed is not a PyFloatObject.
If the object passed is not a PyFloatObject, return -1.
Python environment: 3.4 and higher.
You are not allowed to use PyFloat_AsDouble.
Your function will be tested with this code:
c
Copy code
int main(void)
{
    PyObject *p;

    p = PyFloat_FromDouble(12.34);
    printf("%f\n", c_python_print(p));
    p = PyFloat_FromDouble(1.0 / 0.0);
    printf("%f\n", c_python_print(p));
    p = PyFloat_FromDouble(0.0 / 0.0);
    printf("%f\n", c_python_print(p));
    p = PyLong_FromLong(98);
    printf("%f\n", c_python_print(p));
    return (0);
}
You can find the source code in the provided repository under 0x01-python-if_else_loops_functions/102-magic_calculation.c.
General Instructions
Your code should be written in Python and C, and the Python code should be compatible with version 3.8.5.
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5) and GCC (version 9.3.0).
Your programs and functions should have a standard Python3 shebang (i.e., #!/usr/bin/python3) at the top.
All Python files must be executable.
Your C code should be compiled using the following flags:
c
Copy code
gcc -Wall -Werror -Wextra -pedantic -std=gnu89
All header files must be include guarded.
This project is intended to be completed individually. You may not collaborate with others on this project.
The code you write should adhere to the PEP 8 style guide and the Betty style guide for C.
