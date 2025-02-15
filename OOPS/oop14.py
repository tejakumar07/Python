class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calcualate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    def __repr__(self):
        return 
    



    
item1 = Item('Phone',599,10)
item2 = Item('Laptop',1299,12)
item3 = Item("Keybord", 199,15)
item4 = Item("Mouse",99,25)
item5 = Item('Monitor',399,20)
# This is equal to
# print(Item.all)
'''
for instance in Item.all:
    print(instace.name)
'''


