# 1 parent --> 2 child
# 1 --> child --> child

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

    def show_name(self):
        return self.name

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
       
        """
        Large Algorithm
        """
        return self.text

    def __repr__(self):  # str --> string, repr --> represent
        return f"{self.name} ({self.price})"

    def __str__(self):  # magic method, dunder .. method 
        pass

    
class MobilePhone(Item):
    all = []

    def __init__(self, mbl_name, mbl_price, mblcategory, **kwargs):
        super().__init__(name=mbl_name, price=mbl_price, text=kwargs.get("text", None))
        self.category = mblcategory

        MobilePhone.all.append(self)

    def show_text(self):  # method overriding
        # print(super().show_name())
        return super().show_text()

    def show_category(self):
        return self.category


i1 = Item(name="TV", price=60, text="Korean TV")
mb1 = MobilePhone(mbl_name="MI", mbl_price=50, mblcategory="mobile", text="Chinese Phone")
mb2 = MobilePhone(mbl_name="Samsung", mbl_price=80, mblcategory="mobile", text="Korean Phone")

print(Item.all)
print(MobilePhone.all)

