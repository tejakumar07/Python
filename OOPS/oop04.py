class Item:
    def __init__(self): # It is called Init method or Dunder
        print("I am Created")
        def calculate_total_price(self):
            pass
item1 = Item() # Here It will automatically called init method
item1.name = 'Phone'
item1.price = 500.0
item1.quantity = 5

item2 = Item() # Here also it will called automatically
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3

# Heare it will print I am Created 2 times.