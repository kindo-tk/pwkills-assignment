# main.py (outside the "ecommerce" package)

from products_management import Product
from orders_processing import Order

# Create some products
apple = Product("Apple", 1.99)
banana = Product("Banana", 0.79)

# Create an order
order_items = [apple, banana]
my_order = Order(order_id=123, products=order_items)

print(my_order.calculate_total())  # Calculate the total price
