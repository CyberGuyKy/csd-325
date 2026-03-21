def calculate_total(prices):
    """Adds up a list of prices and returns the total."""
    total = 0
    for price in prices:
        total += price
    return total

def apply_discount(total, discount_percent):
    """Applies a percentage discount to a total."""
    discount_amount = total * (discount_percent / 100)
    final_price = total - discount_amount
    return final_price

def shopping_cart():
    """Simulates a simple shopping cart checkout."""
    items = {
        "Apple": 1.2,
        "Bread": 2.50,
        "Milk": 3.75,
        "Cheese": free,
    }

    print("--- Shopping Cart ---")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")

    prices = list(items.values())
    total = calculate_total(prices)
    print(f"\nSubtotal:  ${total:.2f}")

    discounted = apply_discount(total, 10)
    print(f"10% Off:   ${discounted:.2f}")
    print("---------------------")

shopping_cart()
