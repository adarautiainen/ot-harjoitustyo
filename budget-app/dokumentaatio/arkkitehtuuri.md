# Arkkitehtuurikuvaus

## Pakkausrakenne

Ohjelman koodin pakkausrakenne:

<img width="412" alt="arkkitehtuuri" src="https://user-images.githubusercontent.com/114645764/231719989-e6e21d80-7371-4483-9021-d198ac6ba413.png">

user_interface sisältää käyttöliittymästä vastaavan koodin, service siältää sovelluslogiikasta vastaavan koodin, repos sisältää tietojen pysyväistallennuksesta vastaavan koodin ja budget_user sisältää luokat Budget ja User.

## Käyttöliittymä

Käyttöliittymässä on kolme näkymää: kirjautuminen, uuden käyttäjän luominen ja budjettien listaus. Nämä näkymät on toteutettu omina luokkinaan ja näkymien 
näyttämisestä vastaa luokka UI. Vain yksi näkymä on kerrallaan näkyvänä.

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

Luokka BudgetService käyttää luokkia BudgetRepository ja UserRepository päästääkseen käyttämään käyttäjiä ja budjetteja. Käyttöliittymän toiminnoille luokka BudgetService tarjoaa omat metodit. 
Metodeja on esimerkiksi: 

```login(username, password)```

```create_budget(month, income, expense)```

```get_budgets()```

## Päätoiminnallisuudet sekvenssikaavioina

### Kirjautuminen

Kun käyttäjä syöttää kirjautumisnäkymän käyttäjätunnuksen ja salasanan ja painaa Login-painiketta, sovelluksen kontrolli menee näin:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant BudgetService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>BudgetService: login("maija", "maija789")
  BudgetService->>UserRepository: find_by_user("maija")
  UserRepository-->>BudgetService: user
  BudgetService-->>UI: user
  UI->UI: budgets_show()
```

### Käyttäjän luominen

Kun käyttäjä syöttää uuden käyttäjän luomisnäkymässä käyttäjätunnuksen ja salasanan ja painaa Create user-painiketta, sovelluksen kontrolli menee näin:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant BudgetService
  participant UserRepository
  participant maija
  User->>UI: click "Create user" button
  UI->>BudgetService: create_user("maija", "maija789")
  BudgetService->>UserRepository: find_by_user("maija")
  UserRepository-->>BudgetService: None
  BudgetService->>maija: User("maija", "maija789")
  BudgetService->>UserRepository: create(maija)
  UserRepository-->>BudgetService: user
  BudgetService-->>UI: user
  UI->>UI: budgets_show()
```

### Budjetin luominen

Kun käyttäjä syöttää budjettinäkymässä kuukauden, tulot ja menot, ja painaa Create-painiketta, sovelluksen kontrolli menee näin:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant BudgetService
  participant BudgetRepository
  participant budget
  User->>UI: click "Create"
  UI->>BudgetService: create_budget("may", "1000", "500")
  BudgetService->>budget: Budget("may", "1000", "500", maija)
  BudgetService->>BudgetRepository: create_budget(budget)
  BudgetRepository-->>BudgetService: budget
  BudgetService-->>UI: budget
  UI->>UI: initialize_budget_list()
```

## Tietojen tallennus 

Luokat UserRepository ja BudgetRepository tallentavat tietoja SQLite-tietokantaan. Käyttäjät tallennetaan tauluun users ja budjetit tallennetaan tauluun budgets. Käyttäjien tallennukseen käytettävä taulu alustetaan initialize_database.py-tiedostossa ja budjettien tallennukseen käytettävä taulu alustetaan BudgetRepository-luokassa.
