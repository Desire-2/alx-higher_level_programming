# 0x0F. Python - Object-relational mapping

## Table of Contents
1. [Introduction](#introduction)
2. [Before You Start](#before-you-start)
3. [Background Context](#background-context)
4. [Resources](#resources)
5. [Learning Objectives](#learning-objectives)
6. [Copyright - Plagiarism](#copyright-plagiarism)
7. [Requirements](#requirements)
8. [Install and Activate Virtual Environment](#install-and-activate-virtual-environment)
9. [Tasks](#tasks)
    - [0. Get all states](#0-get-all-states)
    - [1. Filter states](#1-filter-states)
    - [2. Filter states by user input](#2-filter-states-by-user-input)
    - [3. SQL Injection...](#3-sql-injection)
    - [4. Cities by states](#4-cities-by-states)
    - [5. All cities by state](#5-all-cities-by-state)
    - [6. First state model](#6-first-state-model)
    - [7. All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
    - [8. First state](#8-first-state)
    - [9. Contains `a`](#9-contains-a)
    - [10. Get a state](#10-get-a-state)
    - [11. Add a new state](#11-add-a-new-state)
    - [12. Update a state](#12-update-a-state)
    - [13. Delete states](#13-delete-states)
    - [14. Cities in state](#14-cities-in-state)

## Introduction

This project involves working with Object-Relational Mapping (ORM) in Python, specifically using the SQLAlchemy library. The goal is to connect Python scripts with a MySQL database, perform various database operations, and understand the benefits of using an ORM.

## Before You Start

Make sure your MySQL server is in version 8.0. You can find instructions on how to install MySQL 8.0 on Ubuntu 20.04.

## Background Context

In this project, you will use the MySQLdb module to connect to a MySQL database and execute SQL queries. Additionally, you will use the SQLAlchemy module, an Object-Relational Mapper (ORM), to abstract the storage layer and interact with the database using Python code instead of SQL queries.

## Resources

Read or watch:

- [Object-relational mappers](https://realpython.com/object-oriented-programming-python/#object-relational-mappers)
- [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/en/latest/)
- [MySQLdb tutorial](https://www.tutorialspoint.com/python/python_database_access.htm)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/)
- [Introduction to SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://easyaspython.com/sqlalchemy-relationships-explained/)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## Learning Objectives

Upon completing this project, you should be able to explain to anyone without using Google:

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python class to a MySQL table
- How to create a Python Virtual Environment

## Copyright - Plagiarism

You are responsible for solving the tasks below yourself to meet the learning objectives. Copying and pasting someone else’s work is strictly forbidden and will result in removal from the program. Do not publish any content of this project.

## Requirements

- **Allowed editors:** vi, vim, emacs
- **Interpreted/compiled on:** Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- **MySQLdb version:** 2.0.x
- **SQLAlchemy version:** 1.4.x
- **File ending:** All files should end with a new line
- **First line of all files:** `#!/usr/bin/python3`
- **README.md file:** A README.md file at the root of the project folder is mandatory
- **Code style:** Your code should follow PEP 8 guidelines (use pycodestyle version 2.8.*)
- **File execution:** All files must be executable
- **File length:** The length of your files will be tested using `
