import pytest

from models import (
	Food,
	Customer,
	Transaction,
	Menu,
	filter_items_by_category,
	sort_items_by_price,
	compute_transaction_total,
)


def test_order_total_sums_selected_item_prices():
	"""Verify that order total equals the sum of all selected item prices."""
	transaction = Transaction()
	transaction.addItem(Food("Spicy Burger", 8.99, "Entrees", 4.7))
	transaction.addItem(Food("Large Soda", 2.49, "Drinks", 4.2))

	assert compute_transaction_total(transaction) == pytest.approx(11.48)


def test_empty_order_total_is_zero():
	"""Verify that an empty transaction has a total cost of zero."""
	transaction = Transaction()

	assert compute_transaction_total(transaction) == 0


def test_filtering_menu_by_category_returns_only_matching_items():
	"""Verify that filtering by category returns only items from that category."""
	menu = Menu()
	burger = Food("Spicy Burger", 8.99, "Entrees", 4.7)
	soda = Food("Large Soda", 2.49, "Drinks", 4.2)
	water = Food("Bottled Water", 1.99, "Drinks", 4.0)
	menu.addItem(burger)
	menu.addItem(soda)
	menu.addItem(water)

	drinks = filter_items_by_category(menu, "Drinks")

	assert [item.getName() for item in drinks] == ["Large Soda", "Bottled Water"]


def test_filtering_unknown_category_returns_empty_list():
	"""Verify that filtering by a missing category returns an empty list."""
	menu = Menu()
	menu.addItem(Food("Spicy Burger", 8.99, "Entrees", 4.7))

	assert filter_items_by_category(menu, "Desserts") == []


def test_food_rejects_negative_price():
	"""Verify that creating food with a negative price raises a ValueError."""
	with pytest.raises(ValueError):
		Food("Invalid Item", -1.0, "Entrees", 4.0)


def test_food_rejects_empty_name():
	"""Verify that creating food with an empty name raises a ValueError."""
	with pytest.raises(ValueError):
		Food("   ", 5.0, "Entrees", 4.0)


def test_sort_by_price_orders_items_low_to_high():
	"""Verify that sorting by price returns items in ascending order by default."""
	items = [
		Food("Spicy Burger", 8.99, "Entrees", 4.7),
		Food("Large Soda", 2.49, "Drinks", 4.2),
		Food("Chocolate Cake", 5.5, "Desserts", 4.8),
	]

	sorted_items = sort_items_by_price(items)

	assert [item.getName() for item in sorted_items] == [
		"Large Soda",
		"Chocolate Cake",
		"Spicy Burger",
	]


def test_sort_by_price_handles_empty_list():
	"""Verify that sorting an empty list returns an empty list."""
	assert sort_items_by_price([]) == []


def test_remove_missing_item_is_no_op_in_menu_and_transaction():
	"""Verify that removing a missing item does not change menu or transaction state."""
	menu = Menu()
	transaction = Transaction()
	burger = Food("Spicy Burger", 8.99, "Entrees", 4.7)
	soda = Food("Large Soda", 2.49, "Drinks", 4.2)
	menu.addItem(burger)
	transaction.addItem(burger)

	menu.removeItem(soda)
	transaction.removeItem(soda)

	assert [item.getName() for item in menu.getAllItems()] == ["Spicy Burger"]
	assert [item.getName() for item in transaction.getSelectedItems()] == ["Spicy Burger"]


def test_getters_return_copies_for_collections():
	"""Verify that list getters return copies so external mutation does not alter internal state."""
	menu = Menu()
	transaction = Transaction()
	customer = Customer("Yesenia")
	burger = Food("Spicy Burger", 8.99, "Entrees", 4.7)
	menu.addItem(burger)
	transaction.addItem(burger)
	customer.addTransaction(transaction)

	menu_items = menu.getAllItems()
	selected_items = transaction.getSelectedItems()
	history = customer.getPurchaseHistory()

	menu_items.clear()
	selected_items.clear()
	history.clear()

	assert len(menu.getAllItems()) == 1
	assert len(transaction.getSelectedItems()) == 1
	assert len(customer.getPurchaseHistory()) == 1


def test_customer_verification_requires_name_and_history():
	"""Verify that customer verification is true only with non-empty name and purchase history."""
	verified_customer = Customer("Yesenia")
	verified_customer.addTransaction(Transaction())

	unnamed_customer = Customer("   ")
	unnamed_customer.addTransaction(Transaction())

	new_customer = Customer("Yesenia")

	assert verified_customer.isVerified() is True
	assert unnamed_customer.isVerified() is False
	assert new_customer.isVerified() is False
