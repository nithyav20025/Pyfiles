class Order:
    def __init__(self, customer_name, price, quantity, discount=0.0):
        self.name = customer_name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def __final_amount(self):
        return self.price * self.quantity - (1 - self.discount)

    def order_details(self):
        return {
            "Customer Name": self.name,
            "Price": self.price,
            "Quantity": self.quantity,
            "Discount": self.discount,
            "Final Amount": self.__final_amount()
        }


order1 = Order("Nithya", 500, 4, 100)
print(order1.order_details())

