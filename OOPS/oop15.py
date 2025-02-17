class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float,quantity: int ):
        assert price >= 0, f'price is -ve'
        assert quantity >= 0, f'quantity is -ve'
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def __repr__(self):
        # The __repr__ method defines a string representation of the object. When you print an object,
        # Python calls this method to get a readable representation of the object.
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item('Keyboard', 75, 5)
print(Item.all)
# When printing, Python goes through the Item.all list
# and uses each object's __repr__ method to display it.