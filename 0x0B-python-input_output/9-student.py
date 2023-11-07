#!/usr/bin/python3
"""
Module for the Student class.
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        __init__ - Initializes the Student instance.
        to_json - Retrieves a dictionary representation of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student.
        """
        return self.__dict__
