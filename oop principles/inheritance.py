from classes_part3 import Item

class ParentClass:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        return self.name

    def show_age(self):
        return self.age


class ChildClass(ParentClass):  # inherit

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = ParentClass("John", 50)
c1 = ChildClass("Jack", 15)



class MobilePhone(Item):
    all = []

    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        self.discount = kwargs.get("discount", None)
        self.text = kwargs.get("text", None)
        Item.all.append(self)
        MobilePhone.all.append(self)



mp1 = MobilePhone(name="samsung", price=50, text="Samsung Mobile Phone")

print(mp1.show_text())

print(Item.all)
print(MobilePhone.all)

