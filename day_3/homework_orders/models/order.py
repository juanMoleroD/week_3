class Order:
    def __init__(self, product_name, product_description, order_value, customer_name, order_date, quantity):
        self.product_name = product_name
        self.product_description = product_description
        self.order_value = order_value
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity

order_1 = Order("Men's Jacket", "Black, waterproof, stylish", "200.00", "Juan Molero", "07-07-2022", 2)
order_2 = Order("Women's Jacket", "Dark blue, stylish and waterproof", "250.00", "Delia", "10-07-2022", 1)


orders = [order_1, order_2]