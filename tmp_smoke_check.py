from models import (
    Food,
    Customer,
    Transaction,
    Menu,
    filter_items_by_category,
    sort_items_by_price,
    compute_transaction_total,
)


def main():
    burger = Food("Spicy Burger", 8.99, "Entrees", 4.7)
    soda = Food("Large Soda", 2.49, "Drinks", 4.2)
    cake = Food("Chocolate Cake", 5.5, "Desserts", 4.8)
    water = Food("Bottled Water", 1.99, "Drinks", 4.0)

    print("Food objects:")
    print(burger.name, burger.price, burger.category, burger.popularityRating)
    print(soda.name, soda.price, soda.category, soda.popularityRating)
    print(cake.name, cake.price, cake.category, cake.popularityRating)

    menu = Menu()
    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(cake)
    menu.addItem(water)

    print("\nMenu items count:", len(menu.items))
    print("Drinks in menu:", [item.name for item in menu.filterByCategory("Drinks")])
    drinks = filter_items_by_category(menu, "Drinks")
    sorted_by_price = sort_items_by_price(menu.getAllItems())
    print("Drinks via workflow:", [item.name for item in drinks])
    print("Sorted by price:", [item.name for item in sorted_by_price])
    print("Filter check:", [item.name for item in drinks] == ["Large Soda", "Bottled Water"])
    print("Sort check:", [item.name for item in sorted_by_price] == ["Bottled Water", "Large Soda", "Chocolate Cake", "Spicy Burger"])

    transaction = Transaction()
    transaction.addItem(burger)
    transaction.addItem(soda)
    transaction.addItem(water)

    print("\nTransaction selected items:", [item.name for item in transaction.selectedItems])
    print("Transaction total:", transaction.computeTotalCost())
    print("Transaction total via workflow:", compute_transaction_total(transaction))
    expected_total = 8.99 + 2.49 + 1.99
    print("Total check:", round(compute_transaction_total(transaction), 2) == round(expected_total, 2))

    customer = Customer("Yesenia")
    print("\nCustomer verified before purchase:", customer.isVerified())
    customer.addTransaction(transaction)
    print("Customer verified after purchase:", customer.isVerified())
    print("Purchase history length:", len(customer.purchaseHistory))


if __name__ == "__main__":
    main()
