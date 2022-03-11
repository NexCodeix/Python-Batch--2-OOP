class Item:
    all = []
    val = 5
    def __init__(self, name, price, **kwargs):  # constructor function  # initialize
        #  kwargs
        print("Initialized The object")
        self.name = name
        self.price = price
        self.discount = kwargs.get("discount", None)
        self.text = kwargs.get("text", None)
        Item.all.append(self)

    def value_of_item(self):
        a = 5
        return a  # returning "a" because it is being returned

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


if __name__ == "__main__":
    pass
