
class ShoppingCart:
    def __init__(self):
        # Cart items stored as {item_name: {'price': price, 'quantity': quantity}}
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def increment_item(self, name, amount=1):
        if amount <= 0:
            raise ValueError("Increment amount must be positive.")
        if name not in self.items:
            raise KeyError(f"Item '{name}' not in cart.")
        self.items[name]['quantity'] += amount

    def decrement_item(self, name, amount=1):
        if amount <= 0:
            raise ValueError("Decrement amount must be positive.")
        if name not in self.items:
            raise KeyError(f"Item '{name}' not in cart.")
        if self.items[name]['quantity'] <= amount:
            # Remove item if quantity drops to zero or below
            del self.items[name]
        else:
            self.items[name]['quantity'] -= amount

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"Item '{name}' not in cart.")
        del self.items[name]

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_items(self):
        # Returns a copy of the cart items
        return {name: data.copy() for name, data in self.items.items()}
