from cmath import inf
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Rock, Paper, Scissors")
print("What do you choose?")
choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp_choice = random.randint(0, 2)

if choice == 0 and comp_choice == 0:
    print(f"{rock}\n{rock}")
    print("This is a draw. No winner.")

elif choice == 1 and comp_choice == 1:
    print(f"{paper}\n{paper}")
    print("This is a draw. No winner.")
    
elif choice == 2 and comp_choice == 2:
    print(f"{scissors}\n{scissors}")
    print("This is a draw. No winner.")
    
elif choice == 0 and comp_choice == 1:
    print(f"{rock}\n{paper}")
    print("Computer wins.")

elif choice == 1 and comp_choice == 0:
    print(f"{paper}\n{rock}")
    print("You win.")

elif choice == 0 and comp_choice == 2:
    print(f"{rock}\n{scissors}")
    print("You win.")

elif choice == 2 and comp_choice == 0:
    print(f"{scissors}\n{rock}")
    print("Computer wins.")
    

elif choice == 1 and comp_choice == 2:
    print(f"{paper}\n{scissors}")
    print("Computer wins.")

elif choice == 2 and comp_choice == 1:
    print(f"{scissors}\n{paper}")
    print("You win.")

else:
     print("You typed an invalid choice.")     