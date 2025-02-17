import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name, price, quantity):
        assert price >= 0
        assert quantity >= 0
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def discount_applied(self):
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        with open("items17.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item (
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
class Phone(Item):
    pass
phone1 = Item("Iphone",500,5)
phone1.broken_phone = 1
phone2 = Item('Samsung', 499, 5)
phone2.broken_phone = 1