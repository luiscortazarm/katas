def calculate_total_cost(cost_dict, items_bought, tax_rate):
    subtotal = 0
    for item in items_bought:
        # Ignore item if it doesn't exist in the dictionary
        if item in cost_dict:
            subtotal += cost_dict[item]

    total = subtotal * (1 + tax_rate)
    return round(total, 2)


# Example Usage:
costs = {'socks': 5.00, 'shoes': 60.00, 'sweater': 30.00}
cart = ['socks', 'shoes', 'hat']  # 'hat' will be ignored
tax = 0.09  # 9% tax

final_price = calculate_total_cost(costs, cart, tax)
print(final_price)  # Output: 70.85
