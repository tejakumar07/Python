class Iteam:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self): # Here we no need to pass the parameters because we have used self
        return self.quantity * self.price

item1 = Iteam("Phone",500,5) # Object creation
item2 = Iteam('Laptop',1000,3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())