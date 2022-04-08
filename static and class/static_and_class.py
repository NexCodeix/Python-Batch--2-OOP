import csv

class Item:
    all = []
    def __init__(self, name, price, **kwargs):  # constructor function  # initialize
        print("INITIALIZED THE OBJECT")
        self.name = name
        self.price = price
        self.discount = kwargs.get("discount", None)
        self.text = kwargs.get("text", None)
        Item.all.append(self)

    def calculate_total_price(self):
        price = self.price
        if price is None or price == "":
            raise ValueError("Pls provide a price")

        discount = self.discount
        if (discount == "") or (discount is None):
            return price

        total = price - price * discount / 100
        return total


    def change_price(self, new_price):
        self.price  = new_price
        return self.price

    def show_text(self):
        return self.text

    def __repr__(self):  # str --> string, repr --> represent
        return f"{self.name} ({self.price})"

    def __str__(self):  # magic method, dunder .. method 
        pass

    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
            for item in items:
                name = item.get("name")
                cls(name=name, price=int(item.get("price")), text=item.get("text", None))  # cls -> (Item)

    @staticmethod
    def is_integer(a):
        if type(a) == type(5):
            return True

        return False



#  user --> Item.instantiate_from_csv()

Item.instantiate_from_csv()
print(Item.all)

item = Item.all[0]
item.change_price(80)
print(Item.is_integer(10))

