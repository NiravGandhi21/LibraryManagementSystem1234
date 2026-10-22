# Software Requirements Specification (SRS)

## Library Management System

**Version:** 1.0  
**Status:** Initial Draft

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to define the functional and non-functional requirements of the Library Management System. It serves as a reference for development, testing, and future maintenance.

### 1.2 Scope
The Library Management System is designed to simplify library operations by maintaining book records, member information, book issue and return transactions, and book availability.

### 1.3 Intended Audience
- Developers
- Testers
- Library administrators
- Project evaluators

### 1.4 Definitions
- **SRS:** Software Requirements Specification
- **Administrator:** A user who manages library records
- **Member:** A registered library user
- **Issue:** The process of lending a book to a member
- **Return:** The process of recording a borrowed book's return

## 2. Overall Description

### 2.1 Product Perspective
The system is a standalone library management application intended to replace manual record-keeping with organized digital records.

### 2.2 Product Functions
- Add, view, search, update, and remove book records.
- Register and manage members.
- Issue books to registered members.
- Record book returns.
- Display book availability.
- Maintain issue history and due dates.
- Validate input and report errors.

### 2.3 User Classes
**Administrator:** Manages books, members, and borrowing transactions.

**Member:** Searches for books and views availability. Member access to personal borrowing records may be included in a future version.

### 2.4 Operating Environment
- Operating system: Windows, Linux, or macOS
- Programming language: Python
- Testing framework: pytest
- Development environment: Visual Studio Code

### 2.5 Constraints
- The application will be developed using Python.
- Each book and member must have a unique identifier.
- A book cannot be issued when no copy is available.
- Only valid transactions should update library records.

### 2.6 Assumptions and Dependencies
- The administrator enters accurate book and member information.
- The system has sufficient storage for library records.
- Users have access to a supported Python environment.

## 3. Functional Requirements

**FR-01: Add Book**  
The system shall allow the administrator to add a book with a unique ID, title, author, and available-copy count.

**FR-02: View Books**  
The system shall display stored book records.

**FR-03: Search Books**  
The system shall allow searching by title, author, or book ID.

**FR-04: Update Book**  
The system shall allow the administrator to update book details.

**FR-05: Remove Book**  
The system shall allow removal of a book record when removal rules are satisfied.

**FR-06: Register Member**  
The system shall register members with unique member IDs and required details.

**FR-07: Issue Book**  
The system shall issue an available book to a registered member and record the transaction.

**FR-08: Return Book**  
The system shall record a book return and update availability.

**FR-09: Track Due Dates**  
The system shall store and display the due date of each issued book.

**FR-10: Validate Transactions**  
The system shall reject invalid transactions, including issuing unavailable books or issuing books to unregistered members.

## 4. Non-Functional Requirements

**NFR-01: Usability**  
The application shall provide clear instructions and understandable error messages.

**NFR-02: Performance**  
For a small library dataset, common searches should return results within two seconds under normal operating conditions.

**NFR-03: Reliability**  
The system shall maintain consistent book availability when books are issued or returned.

**NFR-04: Maintainability**  
The source code shall be organized into understandable modules and functions.

**NFR-05: Security**  
Administrative operations should be restricted to authorized users when authentication is implemented.

**NFR-06: Portability**  
The application should run on supported operating systems with a compatible Python environment.

## 5. External Interface Requirements

### 5.1 User Interface
The initial version may use a command-line interface with menus, prompts, and status messages.

### 5.2 Software Interface
The application will use Python standard libraries initially. A database may be introduced in a later version if required.

### 5.3 Hardware Interface
The system requires a computer capable of running a supported Python environment.

## 6. Data Requirements

The system shall maintain the following information:

- **Book:** Book ID, title, author, total copies, available copies
- **Member:** Member ID, name, contact details
- **Transaction:** Transaction ID, book ID, member ID, issue date, due date, return date

Unique identifiers shall be used to relate records correctly.

## 7. Acceptance Criteria

The system will be considered acceptable when:

1. The administrator can add and search for books.
2. Duplicate book and member IDs are rejected.
3. Registered members can borrow available books.
4. Unavailable books cannot be issued.
5. Returning a book updates its availability.
6. Invalid inputs produce understandable error messages.
7. Automated tests verify the core requirements.

## 8. Future Enhancements

- User authentication and role-based access
- Fine calculation for overdue books
- Book reservation
- Email or SMS reminders
- Database-backed storage
- Graphical user interface

## 9. Conclusion

This SRS defines the initial requirements and scope of the Library Management System. It provides a foundation for system design, implementation, testing, and maintenance.