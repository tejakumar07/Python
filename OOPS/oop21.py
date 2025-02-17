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
    all = []
    def __init__(self, name, price, quantity, broken_phone = 0):
        # Call to super functions to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phone >= 0
        self.broken_phone = broken_phone
        Item.all.append(self)
phone1 = Phone('Iphone', 500.00, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone('Samsung', 500, 5, 1)