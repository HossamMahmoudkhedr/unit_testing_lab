class InvalidShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        #  No validation for quantity or price
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def increment_item(self, name, amount=1):
        #  No validation for amount or key existence
        self.items[name]['quantity'] += amount

    def decrement_item(self, name, amount=1):
        #  No validation for amount or key existence
        #  No check if item should be removed
        self.items[name]['quantity'] -= amount

    def remove_item(self, name):
        #  No check if item exists
        del self.items[name]

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_items(self):
        return {name: data.copy() for name, data in self.items.items()}
