# Description

This project demonstrates how to organize Python code using modules and custom packages instead of writing everything in a single script. The main goal of Task 4 is to improve code readability, maintainability, and scalability by following proper project structure and modular programming practices.
The project shows how functions can be separated into different files, imported properly, and grouped into a package for better reuse in larger Python applications.

Task4/
│
├── modules/
│   └── myModule.py
│
├── myPackage/
│   ├── __init__.py
│   ├── messages.py
│   └── math.py
│
└── main.py

# Explanation:

modules/myModule.py
Contains multiple reusable methods that are imported into the main file to demonstrate how modules work in Python.

myPackage/
A custom Python package created for this task.

init.py
Makes the folder a Python package so it can be imported.

messages.py
Contains functions related to messages or text output.

math.py
Contains different mathematical utility functions.

main.py
The main script that imports and uses the module and package functions to demonstrate modular programming.

# Modules

The modules directory contains myModule, which groups related functions into a single file. These functions are imported into main.py to show how code can be reused across different files.Using modules helps keep the project organized and avoids writing all logic in one place.

# Custom Package

The myPackage folder is a user-defined Python package. It includes an __init__.py file so Python recognizes it as a package. Inside the package are two modules:messages – Handles message-related functionality.math – Provides mathematical helper functions.This demonstrates how to build and use your own packages in Python projects.

# How to Run

1. Navigate to the Task4 directory.

2. Activate your virtual environment if you created one.

3. Run the main Python file.

The program will execute and demonstrate how modules and packages are imported and used.