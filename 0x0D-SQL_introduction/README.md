# Project Title: 0x0D. SQL - Introduction

## Introduction
This project is part of the ALX Software Engineering program and focuses on introducing SQL (Structured Query Language) and MySQL. The project aims to help you understand the fundamentals of databases, relational databases, and essential SQL operations. The tasks involve creating, modifying, and querying databases and tables using MySQL.

## Project Details
- **Author:** Guillaume
- **Weight:** 1
- **Start Date:** Dec 12, 2023 6:00 AM
- **Deadline:** Dec 15, 2023 6:00 AM
- **Review:** An auto review will be launched at the deadline.

## Concepts
The project covers the following concepts:
- Databases
- MySQL
- SQL
- Database creation and modification
- SQL statements (DDL and DML)
- Subqueries
- MySQL functions
- SQL syntax and techniques

## Resources
Read or watch the provided resources to enhance your understanding:
- [What is Database & SQL?](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL statements: DDL and DML](#)
- [Basic queries: SQL and RA](#)
- [SQL technique: functions](#)
- [SQL technique: subqueries](#)
- [What makes the big difference between a backtick and an apostrophe?](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)
- [Installing MySQL in Ubuntu 20.04](#)

## Learning Objectives
By the end of this project, you are expected to be able to explain:
- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- The meaning of DDL and DML
- How to create or alter a table
- How to select, insert, update, or delete data
- What subqueries are and how to use them
- How to use MySQL functions

## Requirements
- **Allowed Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- **File Endings:** All files should end with a new line
- **SQL Queries:** All SQL queries should have a comment just before
- **File Start:** All files should start with a comment describing the task
- **Keywords:** All SQL keywords should be in uppercase
- **README.md:** A README.md file at the root of the project folder is mandatory
- **File Length:** The length of your files will be tested using `wc`

## How to Use
1. Install MySQL 8.0 on Ubuntu 20.04:
    ```bash
    $ sudo apt update
    $ sudo apt install mysql-server
    $ mysql --version
    ```

2. Connect to your MySQL server:
    ```bash
    $ sudo mysql
    ```

3. Use "container-on-demand" to run MySQL (credentials: root/root):
    ```bash
    $ service mysql start
    $ cat 0-list_databases.sql | mysql -uroot -p
    ```

4. Execute SQL scripts using MySQL command:
    ```bash
    $ cat script_name.sql | mysql -hlocalhost -uroot -p
    ```

## Tasks
### Task 0: List Databases
Write a script that lists all databases of your MySQL server.

Example:
```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

### Task 1: Create a Database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.

Example:
```bash
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

...

## Author
Desire BIKORIMANA
