class Item:
    pay_rate = 0.8 # The Pay rate after the discount
    def __init__(self, name, price, quantity):
        assert price >= 0, f'Price {price} is less than 0'
        assert quantity >= 0, f'Quantity is {quantity} is less than 0'
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculateTotalPrice(self):
        return self.price * self.quantity
item1 = Item("Phone",1239,12)
item2 = Item("Laptop",1769,9)

print(Item.pay_rate)
print(item1.pay_rate) # It will try ro check it form instance level (Line 6, 7 and 8) if it doesn't find there
print(item2.pay_rate) # It will find it from the class level.

print(Item.__dict__) # All the attributes for the class level
print(item1.__dict__)
print(item2.__dict__) # All the attributes for the instance level
 