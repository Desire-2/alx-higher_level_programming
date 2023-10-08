Python - Data Structures: Lists, Tuples
This repository contains Python scripts demonstrating the implementation and manipulation of data structures such as lists and tuples. The tasks aim to reinforce understanding of these fundamental data structures and their usage within Python programming.

Project Details
Author: Guillaume
Weight: 1
Project Start: Oct 6, 2023 6:00 AM
Project End: Oct 10, 2023 6:00 AM
Checker Release: Oct 7, 2023 6:00 AM
Auto Review Deadline: At the project end
Learning Objectives
By the end of this project, you will be able to explain the following concepts to anyone without using external resources:

General
The awesomeness of Python programming.
Understanding and using lists in Python.
Differences and similarities between strings and lists.
Common methods of lists and their usage.
Utilizing lists as stacks and queues.
Understanding and using list comprehensions.
Tuples and their usage.
When to use tuples versus lists.
Understanding sequences in Python.
Tuple packing and sequence unpacking.
The del statement and its usage.
Copyright - Plagiarism
You are required to come up with solutions for the tasks independently to meet the specified learning objectives. Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use pycodestyle (version 2.8.*)
All your files must be executable
C
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The code should use the Betty style and will be checked using betty-style.pl and betty-doc.pl
Not allowed to use global variables
No more than 5 functions per file
Prototypes of all functions should be included in a header file called lists.h
Don’t forget to push your header file
All header files should be include guarded
Resources
You are encouraged to read or watch the following materials:

Lists in Python
Tuples and Sequences in Python
Learn to Program 6 : Lists
Python Object-Oriented Programming (OOP)
Tasks
The project comprises several tasks, each focusing on specific concepts and implementation in Python and C. Each task is associated with a script or C file that you need to complete to meet the learning objectives.

Task 0 - Print a List of Integers
Write a function in Python that prints all integers of a list.
Function prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example for details.
Constraints and requirements:
Do not import any module.
Assume that the list only contains integers.
Use str.format() to print integers.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
Task 1 - Secure Access to an Element in a List
Write a function in Python that retrieves an element from a list.
Function prototype: def element_at(my_list, idx):
Constraints and requirements:
If idx is negative, the function should return None.
If idx is out of range (> number of elements in my_list), the function should return None.
Do not import any module.
Do not use try/except.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
Task 2 - Replace Element
Write a function in Python that replaces an element of a list at a specific position.
Function prototype: def replace_in_list(my_list, idx, element):
Constraints and requirements:
If idx is negative, the function should not modify anything and return the original list.
If idx is out of range (> number of elements in my_list), the function should not modify anything and return the original list.
Do not import any module.
Do not use try/except.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
Task 3 - Print a List of Integers in Reverse
Write a function in Python that prints all integers of a list in reverse order.
Function prototype: def print_reversed_list_integer(my_list=[]):
Constraints and requirements:
Do not import any module.
Assume that the list only contains integers.
Use str.format() to print integers.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
Task 4 - Replace in a Copy
Write a function in Python that replaces an element in a list at a specific position without modifying the original list.
Function prototype: def new_in_list(my_list, idx, element):
Constraints and requirements:
If idx is negative, the function should return a copy of the original list.
If idx is out of range (> number of elements in my_list), the function should return a copy of the original list.
Do not import any module.
Do not use try/except.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
Task 5 - Remove All Characters 'c' and 'C' from a String
Write a function in Python that removes all characters 'c' and 'C' from a string.
Function prototype: def no_c(my_string):
Constraints and requirements:
Do not import any module.
Do not use str.replace().
Example usage:

python
Copy code
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
Task 6 - Lists of Lists = Matrix
Write a function in Python that prints a matrix of integers.
Function prototype: def print_matrix_integer(matrix=[[]]):
Constraints and requirements:
Do not import any module.
Assume that the list only contains integers.
Use str.format() to print integers.
Example usage:

python
Copy code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
Task 7 - Tuples Addition
Write a function in Python that adds two tuples.
Function prototype: def add_tuple(tuple_a=(), tuple_b=()):
Constraints and requirements:
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument.
The second element should be the addition of the second element of each argument.
If a tuple is smaller than 2, use the value 0 for each missing integer.
If a tuple is bigger than 2, use only the first 2 integers.
Do not import any module.
Example usage:

python
Copy code
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
Task 8 - More Returns!
Write a function in Python that returns a tuple with the length of a string and its first character.
Function prototype: def multiple_returns(sentence):
Constraints and requirements:
If the sentence is empty, the first character should be equal to None.
Do not import any module.
Example usage:

python
Copy code
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
Task 9 - Find the Max
Write a function in Python that finds the biggest integer of a list.
Function prototype: def max_integer(my_list=[]):
Constraints and requirements:
If the list is empty, return None.
Do not import any module.
Do not use the builtin max().
Example usage:

python
Copy code
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
Task 10 - Only by 2
Write a function in Python that finds all multiples of 2 in a list.
Function prototype: def divisible_by_2(my_list=[]):
Constraints and requirements:
Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2.
The new list should have the same size as the original list.
Do not import any module.
Example usage:

python
Copy code
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
Task 11 - Delete At
Write a function in Python that deletes the item at a specific position in a list.
Function prototype: def delete_at(my_list=[], idx=0):
Constraints and requirements:
If idx is negative or out of range, nothing should change (returns the same list).
Do not use pop().
Do not import any module.
Example usage:

python
Copy code
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
Task 12 - Switch
Complete the source code in Python to switch the values of two variables, a and b.
The code should be inserted where the comment is (line 4).
The program should be exactly 5 lines long.
Example usage:

python
Copy code
a = 10
b = 89
# Switch the values of a and b here
print("a={:d} - b={:d}".format(a, b))
Task 13 - Linked List Palindrome
Write a function in C that checks if a singly linked list is a palindrome.
Function prototype: int is_palindrome(listint_t **head);
Return 0 if it is not a palindrome, 1 if it is a palindrome.
An empty list is considered a palindrome.
Additional information:
listint_t is a singly linked list structure defined in the provided lists.h file.
Example usage:

c
Copy code
listint_t *head;

head = NULL;
add_nodeint_end(&head, 1);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 1);
print_listint(head);

if (is_palindrome(&head) == 1)
    printf("Linked list is a palindrome\n");
else
    printf("Linked list is not a palindrome\n");

free_listint(head);
Task 14 - CPython #0: Python Lists
Create a C function that prints some basic information about Python lists.
Function prototype: void print_python_list_info(PyObject *p);
Format: see the provided example.
Additional information:
Python version: 3.4
Your shared library will be compiled with this command line:
bash
Copy code
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Example usage:

python
Copy code
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
