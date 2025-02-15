class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name: str, price: float, quantity: int):
        assert price >= 0, f'Price {price} is less than 0'
        assert quantity >= 0, f'Qunatity {quantity} is less than 0'
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
item1 = Item('Phone',599,10)
item2 = Item('Laptop',1299,12)
item3 = Item("Keybord", 199,15)
item4 = Item("Mouse",99,25)
item5 = Item('Monitor',399,20)
item1.apply_discpunt()
item2.pay_rate = 0.7
item3.pay_rate = 0.25
item4.pay_rate = 1.2
item5.pay_rate = 2.2
item2.apply_discount()
item3.apply_discount()
item4.apply_discount()
item5.apply_discount()
print(item1.price)
print(item2.price)
print(item3.price)
print(item4.price)
print(item5.price)

# This will Print Instances for all the Items
print(Item.all)

# It will Print Instances Name
for instances in Item.all:
    print(instances.name)