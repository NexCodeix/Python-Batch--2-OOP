# a = 10

# def local():

#     a = 5
    
#     print("Local a-> ", str(a))

#     return a

# b = local()
# print("Global a-> ", str(a))

def make_global():
    global a
    a = 5



make_global()
print(a)

def make_local():
    a = 10
    print("Local element a is ", str(a))
    

print(a)

make_local()

