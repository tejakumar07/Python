class Item:
    def __init__(self,name: str,price: float,quantity = 0): 
# We restrict the user to enter specific datatype but here quantity = 0 it means that it is int datatype we don't need to mention explicitly
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
item1 = Item('Phone',500,5)
item2 = Item('Laptop',1000,3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())