# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Ashmandeep Kaur

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning.

## Encapsulation
Encapsulation is a key principle of object-oriented programming that involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class.


## Polymorphism
Polymorphism in the `BankAccount` subclasses is achieved by defining a common interface through the `get_service_charges` method. Each subclass, such as `ChequingAccount` and `SavingsAccount`, provides its own implementation of this method according to its specific service charge rules. This allows for dynamic method resolution at runtime, enabling different logic for service charges based on the type of account.

