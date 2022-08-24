import random
# the above allows us to use the random module from python

random_integer = random.randint(1, 10)
print(random_integer)

# import a module of your own
# import my_module
# print("The information below is imported from an own module:")
# print(my_module.pi)


# random float number
random_float = random.random() * 10

print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")