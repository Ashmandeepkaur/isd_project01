# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Ashmandeep Kaur

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning.

Assignment 2: Applying Object-Oriented Design

Assignment 3: Applying Design Patterns

Assignment 4: Programming Paradigms

Assignment 5: Algorithms, Documentation and Distribution

## Encapsulation
Encapsulation is a key principle of object-oriented programming that involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class.


## Polymorphism
Polymorphism in the `BankAccount` subclasses is achieved by defining a common interface through the `get_service_charges` method. Each subclass, such as `ChequingAccount` and `SavingsAccount`, provides its own implementation of this method according to its specific service charge rules. This allows for dynamic method resolution at runtime, enabling different logic for service charges based on the type of account.

## Strategy Pattern
The Strategy Pattern has been applied in this banking application to manage service charge calculations, enhancing flexibility and maintainability. 

-ServiceChargeStrategy: This base class establishes the interface for calculating service charges.

-OverdraftStrategy: A concrete implementation focused on service charges related to overdrafts.

-ManagementFeeStrategy: This strategy calculates management fees based on the age of the account.

-MinimumBalanceStrategy: This class implements the logic for service charges related to minimum balance requirements.

By utilizing the Strategy Pattern, we can easily adapt to future changes in service charge calculations without altering the core bank account classes, thereby adhering to the Open/Closed Principle.

## Observer Pattern

In this banking application, the Observer Pattern is utilized to notify clients of significant activities in their bank accounts. This design pattern allows for a one-to-many relationship between the subjects (bank accounts) and observers (clients), ensuring that any changes in the state of the bank accounts are communicated to the associated clients without tightly coupling their implementations.

### Key Components:

1. Observer: 
   - The `Observer` class defines an interface with an `update` method that concrete observers must implement. This allows different types of observers to respond to notifications from the subject.

2. Subject:
   - The `Subject` class maintains a list of observers and provides methods to attach, detach, and notify them. When an event occurs (such as a transaction that affects the balance), the subject will call the `notify` method to alert all registered observers.

3. Client:
   - The `Client` class, which represents a bank client, inherits from the `Observer` class. When notified of changes in their associated bank accounts, clients receive alerts via email. The `update` method in the `Client` class formats the notification message and uses a simulated email function to send it.

4. BankAccount:
   - The `BankAccount` class acts as the subject in the pattern. It is responsible for maintaining the account's state and notifying clients when significant events occur, such as a low balance or a large transaction. When these conditions are met, the bank account invokes the `notify` method to inform all attached clients.

### Benefits of Using the Observer Pattern:
- Decoupling: Clients are decoupled from the bank account implementation. This allows for greater flexibility and easier maintenance, as changes to the bank account logic do not directly impact the client notification system.
- Scalability: New types of observers (clients) can be added without modifying the existing code, enhancing the scalability of the application.
- Real-time Notifications: Clients receive immediate notifications for important account activities, improving their awareness and ability to manage their finances effectively.

By implementing the Observer Pattern, the application ensures that clients remain informed about critical changes in their bank accounts, enhancing user experience and promoting proactive financial management.



Event-Driven Programming Paradigm:
In this application, the Event-Driven Programming (EDP) paradigm is used to handle user interactions and system responses in a dynamic, responsive manner. The main components of the application are designed to react to events triggered by user actions, such as clicking buttons, selecting rows in tables, or entering data into fields.

Key aspects of EDP in this application include:

1.Signal-Slot Mechanism: The application leverages the signal-slot mechanism in PySide6 (Qt framework) to establish connections between user actions (signals) and corresponding methods (slots). For example, when a user clicks the "Lookup" button, it triggers a signal that connects to the on_lookup_client method, which retrieves and displays client information.

2.Event Handlers: Methods like on_lookup_client, on_select_account, on_apply_transaction, and on_exit serve as event handlers that respond to user actions. Each of these methods processes the user's input, performs the appropriate operations (like retrieving data or updating the interface), and may display messages or open new windows.

3.Real-Time Updates: When a transaction is made (e.g., a deposit or withdrawal), the application updates the relevant data in real time. The AccountDetailsWindow sends a signal to the ClientLookupWindow when a balance changes, ensuring that the client’s bank account details are immediately reflected in the main window.


## Filtering:

Filtering in this application allows users to search and narrow down results based on specific criteria. It is incorporated across various modules, such as clients, transactions, and accounts, enabling users to view only relevant data. The filtering functionality uses dynamic query parameters, allowing for filtering by attributes like client name, account type, transaction date, and amount. This improves the user experience by providing faster access to the information they need, making the application more efficient and user-friendly.