# repeat --> loop 
# age = "20"
# int(age)
#print("My name is MD")

from traceback import print_tb


def call_bio(name, age:int, dob):  # def --> define
    if type(age) != type(60):
        raise ValueError("Pass an integer value")

    print("My name is " + str(name))
    print("My age is " + str(age))
    print("My date of birth is " + str(dob))

# call_bio("Smith", 20, 2000)

# call_bio(name="John", dob="1990", age=50)  
# # call_bio(name="Smith", "1990", age=50)  # after keyword argument we cannot place positional argument
# call_bio("John Doe", dob=1980, age=56)  #  after postitional argument we can place keyword argument


# *args, **kwargs
# def people_bio(name, age, dob, city="Dhaka", country="Bangladesh"):
#     print(f"Name: {name}")
#     print(f"age: {age}")
#     print(f"dob: {dob}")
#     print(f"city: {city}")
#     print(f"country: {country}")
#     print("\n")

# people_bio(name="Suhaib", age=40, dob=1990, country="BD")
# people_bio(name="Safwan", age=40, dob=1990, city="Ctg")


def people_bio(name, *args):
    # args --> list
    print("|Arguments ", args)
    try:

        age = args.__getitem__(0)
    except IndexError:
        age = None

    dob = args[1]  # args[1] = args.__getitem__(1)
    city = args[2]
    country = args.__getitem__(3) 

    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"dob: {dob}")
    print(f"city: {city}")
    print(f"country: {country}")
    print("\n")

#  people_bio("Suhaib", 20, 1995, "Ctg", "BD", "asdasd")  # limitation is it cannot know the position of any value



def people_bio(name, **kwargs):
    # kwargs = dictionary
    print(kwargs)
    age = kwargs.get("age")
    dob = kwargs.get("dob")
    city = kwargs.get("city")
    country = kwargs.get("country")

    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"dob: {dob}")
    print(f"city: {city}")
    print(f"country: {country}")

# people_bio(name="John", age=20, dob=50, country="BD")



# return function

a = 10
b = 20

def total(price1, price2):
    total_price = price1 + price2
    # print(total_price)

    return total_price


