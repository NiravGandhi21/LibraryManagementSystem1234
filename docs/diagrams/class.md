
# Class Diagram — Library Management System

```mermaid
classDiagram
    class Book {
        +String book_id
        +String title
        +String author
        +int total_copies
        +int available_copies
        +update_details()
        +check_availability()
    }

    class Member {
        +String member_id
        +String name
        +String contact
        +view_borrowing_records()
    }

    class Library {
        +add_book()
        +search_book()
        +register_member()
        +issue_book()
        +return_book()
    }

    class Transaction {
        +String transaction_id
        +String book_id
        +String member_id
        +Date issue_date
        +Date due_date
        +Date return_date
        +create_transaction()
        +close_transaction()
    }

    Library ..> Book : manages
    Library ..> Member : registers
    Library ..> Transaction : records
    Member "1" --> "0..*" Transaction : borrows
    Book "1" --> "0..*" Transaction : appears in
```
