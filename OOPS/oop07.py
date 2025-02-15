class Item:
    def __init__(self,name,price,quantity=0): # We can also give parameters in this method
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item('Phone',500)
item2 = Item('Laptop',1000)

print(item1.name) # Phone
print(item1.price) #print phone price
print(item1.quantity) #print Qunatity

print(item2.name)
print(item2.price)
print(item2.quantity)