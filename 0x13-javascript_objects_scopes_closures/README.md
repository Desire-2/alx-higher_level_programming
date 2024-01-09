# Project: 0x13. JavaScript - Objects, Scopes and Closures

## Description
This project focuses on learning and implementing key concepts in JavaScript, such as objects, scopes, closures, and inheritance. The tasks involve creating classes, handling instances, and applying various methods to manipulate objects. The goal is to reinforce understanding of JavaScript programming fundamentals and enhance problem-solving skills.

## Project Timeline
- Start Date: Jan 9, 2024, 6:00 AM
- End Date: Jan 10, 2024, 6:00 AM
- Checker Released: Jan 9, 2024, 12:00 PM
- Auto Review Deadline: Jan 10, 2024, 6:00 AM

## Resources
Read or watch the following resources to gain a deeper understanding:

- [JavaScript object basics](#)
- [Object-oriented JavaScript (read all examples!)](#)
- [Class - ES6](#)
- [super - ES6](#)
- [extends - ES6](#)
- [Object prototypes](#)
- [Inheritance in JavaScript](#)
- [Closures](#)
- [this/self](#)
- [Modern JS](#)

## Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts without the help of Google:

### General
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why variable type and scope are important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Copyright - Plagiarism
- You must come up with solutions for the tasks yourself to meet the learning objectives.
- No copying and pasting of someone else’s work.
- Do not publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using Node (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be semistandard compliant (Rules of Standard + semicolons on top, also as reference: AirBnB style)
- All files must be executable
- The length of files will be tested using `wc`
- You are not allowed to use `var`

### More Info
- Install Node 14:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

- Install `semistandard`:

```bash
$ sudo npm install semistandard --global
```

## Tasks
### 0. Rectangle #0
- Write an empty class `Rectangle` that defines a rectangle using the class notation.

### 1. Rectangle #1
- Write a class `Rectangle` that defines a rectangle using the class notation.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attribute `width` with the value of `w`.
- Initialize instance attribute `height` with the value of `h`.

### 2. Rectangle #2
- Write a class `Rectangle` that defines a rectangle using the class notation.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attribute `width` with the value of `w`.
- Initialize instance attribute `height` with the value of `h`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

### 3. Rectangle #3
- Write a class `Rectangle` that defines a rectangle using the class notation.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attribute `width` with the value of `w`.
- Initialize instance attribute `height` with the value of `h`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
- Create an instance method called `print()` that prints the rectangle using the character `X`.

### 4. Rectangle #4
- Write a class `Rectangle` that defines a rectangle using the class notation.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attribute `width` with the value of `w`.
- Initialize instance attribute `height` with the value of `h`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
- Create an instance method called `print()` that prints the rectangle using the character `X`.
- Create an instance method called `rotate()` that exchanges the width and the height of the rectangle.
- Create an instance method called `double()` that multiplies the width and the height of the rectangle by 2.

### 5. Square #0
- Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`.
- Use the class notation and `extends`.
- Constructor must take 1 argument `size`.
- The constructor of `Rectangle` must be called using `super()`.

### 6. Square #1
- Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`.
- Use the class notation and `extends`.
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`.
- If `c` is undefined, use the character `X`.

### 7. Occurrences
- Write a function that returns the number of occurrences in a list.
- Prototype: `exports.nbOccurences = function (list, searchElement)`

### 8. Esrever
- Write a function that returns the reversed version of a list.
- Prototype: `exports.esrever = function (list)`
- You are not allowed to use the built-in method `reverse`.

### 9. Log me
- Write a function that prints the number of arguments already printed and the new argument value.
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

### 10. Number conversion
- Write a function that converts a number from base 10 to another base passed as an argument.
- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file.
- You are not allowed to declare any new variable (var, let, etc.).

### 11. Factor index (Advanced)
- Write a script that imports an array and computes a new array.
- Your script must import `list` from the file `100-data.js`.
- Use a map.
- A new list must be created with each value equal to the value of the initial list, multiplied by the index in the list.
- Print both the initial list and the new list.

### 12. Sorted occurrences (Advanced)
- Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
- Your script must import `dict` from the

 file `101-data.js`.
- In the new dictionary:
  - A key is a number of occurrences.
  - A value is the list of user ids.
- Print the new dictionary at the end.

### 13. Concat files (Advanced)
- Write a script that concatenates 2 files.
- The first argument is the file path of the first source file.
- The second argument is the file path of the second source file.
- The third argument is the file path of the destination.
