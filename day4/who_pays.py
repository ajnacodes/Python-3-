import random

# create a program that will ask for names then generate a random preson to pay the bill
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# get total number of items in the list
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
# print(random_choice)
person_who_pays = names[random_choice]
print(person_who_pays + " is going to buy the meal today!")
