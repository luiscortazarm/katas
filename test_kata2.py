import pytest
from kata2 import calculate_total_cost

def test_calculate_total_cost():
    costs = {'socks': 5.00, 'shoes': 60.00, 'sweater': 30.00}
    tax = 0.09

    # Shopping cart with valid and invalid items
    cart = ['socks', 'shoes', 'hat']  # 'hat' ignore item
    assert calculate_total_cost(costs, cart, tax) == 70.85

    # Empty shopping cart should return 0.00
    empty_cart = []
    assert calculate_total_cost(costs, empty_cart, tax) == 0.00
