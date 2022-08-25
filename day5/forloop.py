# for loop
# for item in list_of_items:
# Do something to each item

# range
# for number in range(a, b):
#   print(number)

# for number in range(1, 11, 3):
    # print(number)
    # the above function will print numbers from 1 to 11, with a range of 3(it will print numbers from 3 to 3, starting from 1)
    # also called "step size"

total = 0
for number in range(1, 101):
    total += number
print(total)

# add upp even numbers range 1 to 100
total = 0
for number in range(2, 101, 2):
    total += number

print(total)

# another way to add up even numbers:
#  total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)