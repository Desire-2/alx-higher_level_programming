# 0x0C. Python - Almost a Circle

## Description

This project involves the implementation and testing of various Python concepts, including Object-Oriented Programming (OOP), exceptions, classes, private attributes, getter/setter methods, class methods, static methods, inheritance, unittest, and file I/O. The project covers the following topics:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
- Args and kwargs
- Serialization/Deserialization
- JSON

## Background Context

The project is part of the Higher Level Curriculum and serves as preparation for the AirBnB project.

## Learning Objectives

Upon completion of this project, the developer is expected to:

- Understand Unit testing and implement it in a large project
- Know how to serialize and deserialize a Class
- Be able to write and read a JSON file
- Understand and use *args and **kwargs
- Handle named arguments in a function

### Copyright - Plagiarism

Students are reminded that copying and pasting someone else’s work is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All scripts interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- The first line of all files should be exactly `#!/usr/bin/python3`
- Use pycodestyle (version 2.8.*) for code style
- All modules, classes, and functions should be documented
- Python Unit Tests should be implemented using the unittest module

## Tasks

### Task 0: If it's not tested, it doesn't work

- Implement unit tests and ensure PEP 8 validation for all files, classes, and methods.

### Task 1: Base class

- Create a base class with private class attribute `__nb_objects` to manage the `id` attribute in future classes.

### Task 2: First Rectangle

- Write a class `Rectangle` that inherits from the Base class, with private instance attributes, getters, setters, and a constructor.

### Task 3: Validate attributes

- Update the `Rectangle` class to add validation to setter methods and instantiation for width, height, x, and y.

### Task 4: Area first

- Add a public method `def area(self)` to the `Rectangle` class that returns the area value of the instance.

### Task 5: Display #0

- Add a public method `def display(self)` to the `Rectangle` class that prints the Rectangle instance using the character `#`.

### Task 6: \_\_str\_\_

- Override the `__str__` method in the `Rectangle` class to return `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

### Task 7: Display #1

- Improve the `display` method in the `Rectangle` class to consider x and y coordinates.

### Task 8: Update #0

- Add a public method `def update(self, *args)` to the `Rectangle` class that assigns arguments to attributes.

### Task 9: Update #1

- Update the `update` method in the `Rectangle` class to accept key-value arguments.

### Task 10: And now, the Square!

- Write a class `Square` that inherits from `Rectangle` and has the same attributes and methods.

### Task 11: Square size

- Add a public getter and setter `size` to the `Square` class.

### Task 12: Square update

- Add a public method `def update(self, *args, **kwargs)` to the `Square` class to assign arguments to attributes.

### Task 13: Square instance to dictionary representation

- Add a public method `def to_dictionary(self)` to the `Square` class that returns the dictionary representation of a `Square`.

### Task 14: Dictionary to JSON string

- Add a static method `def to_json_string(list_dictionaries)` to the `Base` class that returns the JSON string representation of a list of dictionaries.

### Task 15: JSON string to file

- Add a class method `def save_to_file(cls, list_objs)` to the `Base` class that writes the JSON string representation of a list of instances to a file.

### Task 16: JSON string to dictionary

- Add a static method `def from_json_string(json_string)` to the `Base` class that returns the list of the JSON string representation.

### Task 17: Dictionary to Instance

- Add a class method `def create(cls, **dictionary)` to the `Base` class that returns an instance with all attributes set.

### Task 18: File to instances

- Add a class method `def load_from_file(cls)` to the `Base` class that returns a list of instances.

## Usage

Clone the repository and run the tests:

```bash
$ git clone

