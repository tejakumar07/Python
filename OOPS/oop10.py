class Item:
    def __init__(self,name: str, price: float, quantity: int):
        # Run the Validations to receive the arguments
        assert price >= 0, f"Price {price} is not less than 0"
        self.name = name, f'Quantity is less than 0'
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
item1 = Item('Phone',200,13)
item2 = Item('Laptop',1299,7)
print(item1.calculate_total_price())
print(item2.calculate_total_price())