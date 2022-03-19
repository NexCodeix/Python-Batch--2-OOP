import csv


class Item:
    all = []

    def __init__(self, name, price, **kwargs):  # constructor function  # initialize
        assert price>0, "Price should be more than 0"
        self.__name = name
        self.price = price
        self.discount = kwargs.get("discount", None)
        self.text = kwargs.get("text", None)
        Item.all.append(self)

    def show_name(self):
        return self.__name

    @property  # read only method
    def name(self):
        return self.__name

    @name.setter  # we will set a value for this
    def name(self, new_name):
        print("Changing name via setter")
        self.change_name(new_name)  # set_name --> change_name --> new_name 

    def change_name(self, new_name):
        if len(new_name) > 5:
            raise ValueError("Length must be less than 5")
            
        self.__name = new_name
        return new_name

    def give_info(self):
        return f"{self.__name} {self.price}"

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

    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
            for item in items:
                name = item.get("name")
                cls(name=name, price=int(item.get("price")), text=item.get("text", None))  # cls -> (Item)

    def show_text(self):
        return self.text

    def __repr__(self):  # str --> string, repr --> represent
        return f"{self.__name} ({self.price})"

    def __str__(self):  # magic method, dunder .. method 
        pass

    def __connect(self, smtp_server):
        print(f"CONNECTING TO {smtp_server}")

    def __prepare_body(self):
        print("PREPARING BODY FOR EMAIL")
        return f"""
        {self.__name} Item has been added to our company.
        """

    def send_email(self):
        self.__connect("127.0.0.1")
        self.__prepare_body()
        self.__send()

    def __send(self):
        print("SENDING EMAIL TO THE USER \n")



Item.instantiate_from_csv()
# Abstraction   # class level -- > function_call but not in instance level

# item1.send_email()


