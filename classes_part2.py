
class Item:
    
    def __init__(self, name, price, **kwargs):  # constructor function  # initialize
        #  kwargs
        print("Initialized The object")
        self.name = name
        self.price = price
        self.discount = kwargs.get("discount", None)
        self.text = kwargs.get("text", None)

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


item1 = Item(name="Shirt", price=50, discount=10, text="Hello")  # Item().__init__()
# item1.name = "Shirt"
# item1.price = 50
# item1.discount = 10

# item1.change_price(40)

total = item1.calculate_total_price()
print("TOTal price ", str(total))
print(item1.show_text())
print("\n")

