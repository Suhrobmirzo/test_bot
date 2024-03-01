# from collections import namedtuple 
# User = namedtuple("user","id name l_name age emile")

# users = [
#     (1, "a", "a" , 1, "as"),
#     (1, "b", "b" , 2, "bs"),
# ]

# for user in users:
#     us = User(*user)
#     print(*us)


from collections import namedtuple 
Car = namedtuple("Car", "name rangi tezlik narx orindiq rusumi")

cars = ('malibu', 'rangi', '300km', 20000, 4, "turbo")

c = Car(*cars)

print(c.name)

# print(cars[0])

