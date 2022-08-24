import random
# the above allows us to use the random module from python

random_integer = random.randint(1, 10)
print(random_integer)

# import a module of your own
import my_module
print("The information below is imported from an own module:")
print(my_module.pi)