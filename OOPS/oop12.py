class Item:
    pay_rate = 0.8 # The Pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity: int):

        assert price >= 0, f'Price {price} is less than 0'
        assert quantity >=0, f'Quantity {quantity} is less than 0'
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate # If we apply self here it always apply default pay_rate is =0.8
        # if we want to change the pay rate for instance level it is best pratice to use 'self'                  
item1 =Item('Phone',100.0,1)
item1.apply_discount()
print(item1.price)
item2 =Item("Laptop",1000.0,3)
item2.pay_rate =0.7
item2.apply_discount()
print(item2.price)
