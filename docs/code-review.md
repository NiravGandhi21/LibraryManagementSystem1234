# Practical 9: Code Review Report

## Aim
To review the Library Management System code using a checklist covering naming, modularity, error handling, readability, and test coverage.

## Review Checklist

| Criterion | Observation |
|---|---|
| Naming | Class and method names are meaningful. |
| Modularity | Book insertion and searching are separate methods. |
| Error handling | Duplicate IDs, negative copies, and invalid fields are rejected. |
| Readability | Consistent indentation and a simple dictionary structure improve readability. |
| Test coverage | Tests cover adding books, searching, duplicate IDs, negative copies, zero copies, empty titles, and non-integer copies. |

## Improvements Made
1. Added validation for empty book IDs, titles, and author names.
2. Added integer validation for copy counts.
3. Added tests for zero copies and invalid input.
4. Verified that rejected input does not add a book to the catalog.

## Result
The Library Management System was reviewed and improved using a code review checklist. Additional validation and automated tests were added to improve reliability and maintainability.