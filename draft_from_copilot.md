classDiagram
    class Food {
        -name: String
        -price: double
        -category: String
        -popularityRating: double
        +Food(name, price, category, popularityRating)
        +getName(): String
        +getPrice(): double
        +getCategory(): String
        +getPopularityRating(): double
    }

    class Customer {
        -customerId: String
        -name: String
        -purchaseHistory: List~Transaction~
        +Customer(customerId, name)
        +addTransaction(t: Transaction): void
        +getPurchaseHistory(): List~Transaction~
        +isVerified(): boolean
    }

    class Transaction {
        -transactionId: String
        -items: List~Food~
        -timestamp: DateTime
        +Transaction(transactionId)
        +addItem(item: Food): void
        +removeItem(item: Food): void
        +getItems(): List~Food~
        +getTotalCost(): double
    }

    class Menu {
        -items: List~Food~
        +addItem(item: Food): void
        +removeItem(item: Food): void
        +getAllItems(): List~Food~
        +filterByCategory(category: String): List~Food~
        +searchByName(name: String): List~Food~
    }

    Customer "1" --> "0..*" Transaction : has
    Transaction "1" *-- "1..*" Food : contains
    Menu "1" o-- "0..*" Food : lists