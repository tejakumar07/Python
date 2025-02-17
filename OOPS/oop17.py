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
'''
1️⃣ If num is a float:
It checks if num is a whole number using num.is_integer().
print(Item.is_integer(7.0))  # True (7.0 is like 7)
print(Item.is_integer(7.5))  # False (7.5 has a decimal part)

2️⃣ If num is an int, return True immediately.
print(Item.is_integer(9))  # True (9 is already an integer)

3️⃣ If num is not a float or int, return False.
print(Item.is_integer("hello"))  # False
print(Item.is_integer([1, 2, 3]))  # False

'''

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.5))
print(Item.is_integer(7.0))
print(Item.is_integer(9))