class Food:
	def __init__(self, name, price, category, popularityRating):
		if not isinstance(name, str) or not name.strip():
			raise ValueError("name must be a non-empty string")
		if not isinstance(category, str) or not category.strip():
			raise ValueError("category must be a non-empty string")
		if not isinstance(price, (int, float)) or price < 0:
			raise ValueError("price must be a non-negative number")
		if not isinstance(popularityRating, (int, float)) or popularityRating < 0:
			raise ValueError("popularityRating must be a non-negative number")

		self.name = name
		self.price = price
		self.category = category
		self.popularityRating = popularityRating

	def getName(self):
		return self.name

	def getPrice(self):
		return self.price

	def getCategory(self):
		return self.category

	def getPopularityRating(self):
		return self.popularityRating


class Customer:
	def __init__(self, name):
		self.name = name
		self.purchaseHistory = []

	def addTransaction(self, transaction):
		self.purchaseHistory.append(transaction)

	def getPurchaseHistory(self):
		return self.purchaseHistory.copy()

	def isVerified(self):
		has_name = isinstance(self.name, str) and bool(self.name.strip())
		has_history = len(self.purchaseHistory) > 0
		return has_name and has_history


class Transaction:
	def __init__(self):
		self.selectedItems = []

	def addItem(self, item):
		self.selectedItems.append(item)

	def removeItem(self, item):
		if item in self.selectedItems:
			self.selectedItems.remove(item)

	def getSelectedItems(self):
		return self.selectedItems.copy()

	def computeTotalCost(self):
		return sum(item.getPrice() for item in self.selectedItems)


class Menu:
	def __init__(self):
		self.items = []

	def addItem(self, item):
		self.items.append(item)

	def removeItem(self, item):
		if item in self.items:
			self.items.remove(item)

	def getAllItems(self):
		return self.items.copy()

	def filterByCategory(self, category):
		return [item for item in self.items if item.getCategory() == category]


def filter_items_by_category(menu, category):
	# Return all menu items that belong to the given category.
	return menu.filterByCategory(category)


def sort_items_by_price(items, descending=False):
	# Return items sorted by price.
	return sorted(items, key=lambda item: item.getPrice(), reverse=descending)


def compute_transaction_total(transaction):
	# Return the total cost of all selected items in a transaction.
	return transaction.computeTotalCost()