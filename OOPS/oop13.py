class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f'Price: {price} is -ve'
        assert quantity >= 0, f'Quantity {quantity} is -ve'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)     

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item('Keyboard', 75, 5)

# This will print 5 instances for 5 items
print(Item.all)

# This will print all the Item Names of Instances
for instance in Item.all:
    print(instance.name)
