# Arkkitehtuurikuvaus

## Pakkausrakenne

<img width="412" alt="arkkitehtuuri" src="https://user-images.githubusercontent.com/114645764/231719989-e6e21d80-7371-4483-9021-d198ac6ba413.png">

## Sovelluslogiikka

Käyttäjiä ja käyttäjien budjetteja kuvaavat luokat User ja Budget:
```mermaid
classDiagram
  Budget "*" --> "1" User
      class User{
          username
          password
      }
      class Budget{
          month
          income
          expense
          budget_id
      }
```

## Sekvenssikaavio

### Budjetin luominen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant BudgetService
  participant BudgetRepository
  participant budget
  User->>UI: click "Create"
  UI->>BudgetService: create_budget("may", "1000", "500€")
  BudgetService->>budget: Budget("may", "1000", "500", maija)
  BudgetService->>BudgetRepository: create_budget(budget)
  BudgetRepository-->>BudgetService: budget
  BudgetService-->>UI: budget
  UI->>UI: initialize_budget_list()
```
