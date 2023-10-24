*  0x06. Python - Classes and Objects
Overview
This project is part of the "Holberton School" curriculum and covers the fundamentals of Object-Oriented Programming (OOP) in Python. It will help you understand the concept of classes and objects and their various attributes and methods.

Project Details
Project Name: 0x06. Python - Classes and Objects
Language: Python
Topics: Object-Oriented Programming (OOP)
Author: Guillaume
Weight: 1
Start Date: October 24, 2023, 6:00 AM
End Date: October 25, 2023, 6:00 AM
Checker Release Date: October 24, 2023, 12:00 PM
Auto Review: A review will be launched at the deadline.
Background Context
Object-Oriented Programming (OOP) is a fundamental concept in programming, and this project introduces you to its basics. It is crucial that you read the provided resources and experiment with OOP on your own. You are expected to learn the following:

Why Python programming is awesome
What is OOP
"First-class everything"
What is a class
What is an object and an instance
The difference between a class and an object or instance
What is an attribute
How to use public, protected, and private attributes
What is self
What is a method
The special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
The difference between an attribute and a property in Python
The Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to objects and classes
What is the __dict__ of a class and/or instance of a class and what does it contain
How Python finds the attributes of an object or class
How to use the getattr function
Copyright and Plagiarism
Plagiarism is strictly forbidden in this project. You are required to come up with solutions to the tasks yourself, and copying and pasting someone else's work is not allowed. You are also not allowed to publish any content from this project.

** Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Your code should use pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__))
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__))
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__) and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__))
A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method.
* Tasks
** 0. My first square
Create an empty class Square that defines a square. You are not allowed to import any modules.

** 1. Square with size
Write a class Square that defines a square with a private instance attribute size. The instantiation should be done with a size (no type or value verification). You are not allowed to import any modules.

** 2. Size validation
Add validation to the Square class. Define a private instance attribute size, which can be set during instantiation with an optional size argument. The size attribute must be an integer, and if it's less than 0, it should raise a ValueError with the message "size must be >= 0". You are not allowed to import any modules.

** 3. Area of a square
Add a public instance method def area(self): to the Square class that returns the current square area. You should also add validation for the size attribute, following the same rules as in task 2. You are not allowed to import any modules.

** 4. Access and update private attribute
In the Square class, create a property def size(self): to retrieve the size attribute and a property setter def size(self, value): to set it. The size attribute must be an integer, and if it's less than 0, it should raise a ValueError with the message "size must be >= 0". You should also define a public instance method def area(self): that returns the current square area. You are not allowed to import any modules.

** 5. Printing a square
Extend the Square class by adding a public instance method def my_print(self): that prints the square using the # character. If the size is equal to 0, it should print an empty line. You are not allowed to import any modules.

** 6. Coordinates of a square
Add a private instance attribute position to the Square class. The attribute must be a tuple of two positive integers, and if it doesn't meet this condition, it should raise a TypeError with the message "position must be a tuple of 2 positive integers". The position attribute represents the position of the square on a 2D plane. When printing the square, use spaces to fill lines when position[1] is greater than 0. You are not allowed to import any modules.

** 7. Singly linked list (Advanced)
Create a class Node that defines a node of a singly linked list with a private instance attribute data and a private instance attribute next_node. The data attribute must be an integer, and the next_node attribute must be either a Node object or None. Create a class SinglyLinkedList that defines a singly linked list. The SinglyLinkedList class should have a private instance attribute head, which is the first node of the singly linked list.

The SinglyLinkedList class should be able to print the entire list, with one node number per line. It should also have a public instance method def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list in increasing order.

** 8. Print Square instance (Advanced)
Add a __str__ method to the Square class that defines the behavior of the square instance when it's printed. The square should be printed using the # character, and if the size is equal to 0, it should print an empty line. The position attribute should be used to position the square, and spaces should be used to fill lines when position[1] is greater than 0.

** 9. Compare 2 squares (Advanced)
Extend the Square class with the ability to compare two square instances. Implement the following comparators: ==, !=, >, >=, <, and <=. The comparison should be based on the square's area.

** 10. ByteCode -> Python #5 (Advanced)
Create a Python class MagicClass that replicates the behavior of the provided Python bytecode. The bytecode is a series of instructions that define the class MagicClass. Your task is to implement the same functionality in Python code.

** Conclusion
This project will help you understand and practice the basics of Object-Oriented Programming (OOP) in Python. By completing the tasks, you will gain a deeper understanding of classes, objects, attributes, and methods, as well as how to manipulate and work with them in Python. Good luck with your project!
