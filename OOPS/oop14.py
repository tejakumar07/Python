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
        return 'Item'

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item('Keyboard', 75, 5)
print(Item.all)