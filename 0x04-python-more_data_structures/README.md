0x04. Python - More Data Structures: Set, Dictionary
This is a project in which you will be working with Python's sets and dictionaries, as well as functions and data manipulation. Below are the tasks to be completed.

Learning Objectives
After completing this project, you should be able to:

Understand the use of sets and dictionaries in Python.
Differentiate when to use sets versus lists and dictionaries.
Write functions to perform operations on data structures.
Write code that follows PEP8 style guidelines.
Requirements
All your Python code should be written using Python 3 (version 3.8.5).
You are allowed to use only the following editors: vi, vim, or emacs.
All your files must be interpreted and compiled on Ubuntu 20.04 LTS.
Your code should use the PEP8 style (version 2.8.*) and should end with a new line.
The first line of all your files should be exactly #!/usr/bin/python3.
All your files must be executable.
The length of your files will be tested using wc.
Project Tasks
0. Squared simple
Write a function square_matrix_simple that computes the square value of all integers in a matrix. The function should meet the following requirements:

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2-dimensional array.
Returns a new matrix with the same size as the input.
Each value in the new matrix should be the square of the corresponding value in the input matrix.
The initial matrix should not be modified.
You are not allowed to import any modules.
You are allowed to use regular loops, map, etc.
1. Search and replace
Write a function search_replace that replaces all occurrences of an element with another element in a new list. The function should meet the following requirements:

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list.
search is the element to replace in the list.
replace is the new element.
You are not allowed to import any modules.
2. Unique addition
Write a function uniq_add that adds all unique integers in a list, taking each integer only once. The function should meet the following requirements:

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any modules.
3. Present in both
Write a function common_elements that returns a set of common elements in two sets. The function should meet the following requirements:

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any modules.
4. Only differents
Write a function only_diff_elements that returns a set of all elements that are present in only one of two sets. The function should meet the following requirements:

Prototype: def only_diff_elements(set_1, set_2):
You are not allowed to import any modules.
5. Number of keys
Write a function number_keys that returns the number of keys in a dictionary. The function should meet the following requirements:

Prototype: def number_keys(a_dictionary):
You are not allowed to import any modules.
6. Print sorted dictionary
Write a function print_sorted_dictionary that prints a dictionary sorted by its keys. The function should meet the following requirements:

Prototype: def print_sorted_dictionary(a_dictionary):
You can assume that all keys are strings.
Keys should be sorted in alphabetic order.
Only sort keys of the first level (don't sort keys of a dictionary inside the main dictionary).
Dictionary values can have any type.
You are not allowed to import any modules.
7. Update dictionary
Write a function update_dictionary that replaces or adds a key/value pair in a dictionary. The function should meet the following requirements:

Prototype: def update_dictionary(a_dictionary, key, value):
The key argument will always be a string.
The value argument can be any type.
If a key exists in the dictionary, the value will be replaced.
If a key doesn't exist in the dictionary, it will be created.
You are not allowed to import any modules.
8. Simple delete by key
Write a function simple_delete that deletes a key from a dictionary. The function should meet the following requirements:

Prototype: def simple_delete(a_dictionary, key=""):
The key argument will always be a string.
If the key doesn't exist in the dictionary, the dictionary won't change.
You are not allowed to import any modules.
9. Multiply by 2
Write a function multiply_by_2 that returns a new dictionary with all values multiplied by 2. The function should meet the following requirements:

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are integers.
Returns a new dictionary.
You are not allowed to import any modules.
10. Best score
Write a function best_score that returns the key with the highest integer value in a dictionary. The function should meet the following requirements:

Prototype: def best_score(a_dictionary):
You can assume that all values are integers.
If no score is found, return None.
You can assume all keys have a different score.
You are not allowed to import any modules.
11. Multiply by using map
Write a function multiply_list_map that returns a new list with all values multiplied by a given number without using loops. The function should meet the following requirements:

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list with the same length as my_list.
Each value in the new list should be the result of multiplying the corresponding value in my_list by number.
The initial list should not be modified.
You have to use map.
You are not allowed to use for or while loops.
Your code should be no longer than 3 lines.
12. Roman to Integer
Create a function roman_to_int that converts a Roman numeral to an integer. The function should meet the following requirements:

Prototype: def roman_to_int(roman_string):
roman_string is the Roman numeral to be converted.
The function should return an integer.
If roman_string is not a string or is None, the function should return 0.
13. Weighted average!
Write a function weight_average that returns the weighted average of a list of tuples, each containing a score and a weight. The function should meet the following requirements:

Prototype: def weight_average(my_list=[]):
The function should return 0 if the list is empty.
You are not allowed to import any modules.
14. Squared by using map
Write a function square_matrix_map that computes the square value of all integers in a matrix using map. The function should meet the following requirements:

Prototype: def square_matrix_map(matrix=[]):
matrix is a 2-dimensional array
