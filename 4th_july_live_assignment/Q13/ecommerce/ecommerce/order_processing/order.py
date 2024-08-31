class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products
        self.status = 'Pending'

    def __repr__(self):
        return f"Order(order_id={self.order_id}, products={self.products}, status={self.status})"

def create_order(order_id, products):
    return Order(order_id, products)
