def calculate_total(products):
    return sum(product.price for product in products)

def format_currency(amount):
    return f"${amount:.2f}"
