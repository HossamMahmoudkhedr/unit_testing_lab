import pytest
# switch between invalid class and valid one 
# from invalid_shopping_cart import InvalidShoppingCart
from shopping_cart import ShoppingCart

@pytest.mark.parametrize("name, price, quantity, expected", [
    ('apple', 1.5, 2, {'apple': {'price': 1.5, 'quantity': 2}}),
    ('banana', 2.0, 1, {'banana': {'price': 2.0, 'quantity': 1}})
])
def test_add_item_valid(name, price, quantity, expected):
    cart = ShoppingCart()
    cart.add_item(name, price, quantity)
    assert cart.get_items() == expected


@pytest.mark.parametrize("name, price, quantity", [
    ('banana', 0.5, 0),
    ('banana', 0.5, -3)
])
def test_add_item_invalid_quantity(name, price, quantity):
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(name, price, quantity)


@pytest.mark.parametrize("name, price, quantity", [
    ('banana', -1.0, 2)
])
def test_add_item_invalid_price(name, price, quantity):
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(name, price, quantity)


@pytest.mark.parametrize("initial_qty, increment, expected", [
    (1, 3, 4),
    (2, 2, 4)
])
def test_increment_item_valid(initial_qty, increment, expected):
    cart = ShoppingCart()
    cart.add_item('apple', 1.5, initial_qty)
    cart.increment_item('apple', increment)
    assert cart.get_items()['apple']['quantity'] == expected


@pytest.mark.parametrize("initial_items, item, inc, error", [
    ({}, 'orange', 2, KeyError),
    ({'apple': (1.5, 1)}, 'apple', 0, ValueError),
    ({'apple': (1.5, 1)}, 'apple', -1, ValueError)
])
def test_increment_item_invalid(initial_items, item, inc, error):
    cart = ShoppingCart()
    for k, (p, q) in initial_items.items():
        cart.add_item(k, p, q)
    with pytest.raises(error):
        cart.increment_item(item, inc)
        
        
@pytest.mark.parametrize("start_qty, dec1, dec2, expected", [
    (5, 2, 3, {})
])
def test_decrement_item_valid(start_qty, dec1, dec2, expected):
    cart = ShoppingCart()
    cart.add_item('apple', 1.5, start_qty)
    cart.decrement_item('apple', dec1)
    cart.decrement_item('apple', dec2)
    assert cart.get_items() == expected


@pytest.mark.parametrize("initial_items, item, dec, error", [
    ({}, 'banana', 1, KeyError),
    ({'banana': (2.0, 2)}, 'banana', 0, ValueError),
    ({'banana': (2.0, 2)}, 'banana', -2, ValueError)
])
def test_decrement_item_invalid(initial_items, item, dec, error):
    cart = ShoppingCart()
    for k, (p, q) in initial_items.items():
        cart.add_item(k, p, q)
    with pytest.raises(error):
        cart.decrement_item(item, dec)


@pytest.mark.parametrize("items_to_add, remove_item, expected", [
    ([('apple', 1.5, 2), ('banana', 2.0, 1)], 'apple', {'banana': {'price': 2.0, 'quantity': 1}})
])
def test_remove_item_valid(items_to_add, remove_item, expected):
    cart = ShoppingCart()
    for name, price, qty in items_to_add:
        cart.add_item(name, price, qty)
    cart.remove_item(remove_item)
    assert cart.get_items() == expected


@pytest.mark.parametrize("item", ['orange'])
def test_remove_item_invalid(item):
    cart = ShoppingCart()
    with pytest.raises(KeyError):
        cart.remove_item(item)

@pytest.mark.parametrize("items, expected_total", [
    ([('apple', 1.5, 2), ('banana', 2.0, 3)], 1.5*2 + 2.0*3),
])
def test_total_price(items, expected_total):
    cart = ShoppingCart()
    for name, price, qty in items:
        cart.add_item(name, price, qty)
    assert cart.total_price() == pytest.approx(expected_total)


def test_cart_sequence():
    cart = ShoppingCart()
    cart.add_item('apple', 1.5, 2)
    cart.add_item('banana', 2.0, 1)
    cart.increment_item('banana', 2)
    cart.decrement_item('apple', 1)
    cart.remove_item('banana')
    assert cart.get_items() == {'apple': {'price': 1.5, 'quantity': 1}}

