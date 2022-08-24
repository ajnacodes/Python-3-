# 🚨 Don't change the code below 👇
# leap year calculator
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_calc = year % 4
second_calc = year % 100
third_calc = year % 400 

if first_calc == 0:
    if second_calc == 0:
        if third_calc == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")  