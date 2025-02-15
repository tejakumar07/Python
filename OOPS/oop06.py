class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item('Phone',500,5)
item2 = Item('Laptop',1000,3)

print(item1.name) # Phone
print(item1.price) #print phone price
print(item1.quantity) #print Qunatity

print(item2.name)
print(item2.price)
print(item2.quantity)