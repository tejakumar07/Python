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
        with open("items16.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item (
                name = item.get('name'), # item.get('name') returns None if the key is missing, preventing an error
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)