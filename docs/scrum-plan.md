# Practical 5: Agile Project Management Using Scrum

## 1. Aim
To apply Scrum principles to plan and manage the development of a Library Management System.

## 2. Product Vision
To develop a simple and reliable application that helps a library manage books, members, and borrowing transactions efficiently.

## 3. Scrum Roles
- Product Owner: Prioritizes requirements and defines product value.
- Scrum Master: Facilitates Scrum activities and helps remove obstacles.
- Developers: Design, implement, and test the selected functionality.

## 4. Product Backlog

| ID | Product Backlog Item | Priority | Acceptance Criteria |
|---|---|---|---|
| PBI-01 | Add a book | High | A book with valid details can be saved with a unique ID |
| PBI-02 | View all books | High | Stored books can be displayed |
| PBI-03 | Search books | High | Books can be found by ID or title |
| PBI-04 | Register a member | High | A member can be registered with a unique ID |
| PBI-05 | Issue a book | High | An available book can be issued to a registered member |
| PBI-06 | Return a book | High | A return updates book availability |
| PBI-07 | Validate inputs | Medium | Invalid inputs are rejected with clear messages |
| PBI-08 | Track due dates | Medium | Issue records include a due date |
| PBI-09 | Calculate overdue fines | Low | Overdue returns can be assessed according to a defined policy |
| PBI-10 | Add user authentication | Low | Restricted operations require authorized access |

## 5. Sprint Planning

**Sprint duration:** One week

**Sprint Goal:** Deliver the initial book catalog and member registration functionality.

### Selected Sprint Backlog
1. Implement adding a book.
2. Implement viewing all books.
3. Implement searching by book ID or title.
4. Implement member registration.
5. Validate required fields and unique IDs.
6. Write tests for the selected functionality.
7. Review and document the completed work.

### Definition of Done
A backlog item is considered done when:
- Its implementation is complete.
- Input validation is included where required.
- Relevant automated tests pass.
- The code is reviewed.
- The changes are committed to version control.
- Acceptance criteria are satisfied.

## 6. Sprint Execution

The team checks progress during a Daily Scrum. Each participant discusses:
- Progress toward the Sprint Goal.
- Work planned next.
- Obstacles affecting progress.

The team updates the Sprint Backlog as it learns more, without compromising the Sprint Goal.

## 7. Sprint Review

At the end of the sprint, the team demonstrates the completed features to stakeholders and collects feedback.

**Review checklist:**
- Can a book be added?
- Can stored books be displayed?
- Can books be searched?
- Can a member be registered?
- Are invalid and duplicate IDs handled correctly?

The team records feedback and updates the Product Backlog when appropriate.

## 8. Sprint Retrospective

The team discusses what went well, what caused problems, and what should improve in the next sprint.

**Example retrospective:**

### What went well
- Tasks were divided into manageable items.
- Requirements were documented before implementation.
- Git was used to track changes.

### What could be improved
- Tasks should have clearer estimates.
- Testing should begin alongside implementation.
- Merge conflicts should be addressed early.

### Action items
- Write acceptance criteria before starting each task.
- Run automated tests before committing changes.
- Review task progress during the Daily Scrum.

These are example observations for the practical; replace them with actual observations after conducting your sprint.

## 9. Expected Outcome
The team plans an achievable sprint, maintains a prioritized Product Backlog, defines completion criteria, and uses review and retrospective activities to improve delivery.

## 10. Conclusion
Scrum provides an iterative and collaborative approach to software development. Product Backlog prioritization, Sprint Planning, regular progress inspection, Sprint Reviews, and Retrospectives help the team deliver useful functionality and improve its working process.