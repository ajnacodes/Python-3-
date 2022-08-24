# Welcome to the treasure island project!
print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ '
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|                                 
  _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                 _                                                
                ;`',                                              
                `,  `,                                     
                 ',   ;   ,,-""==..,                      
                  \    ','          '.                     
          ,-""'-., ;    '    __.-="-.;                      
        ," ,,_    "V      _."                              
       ;,'   ''-,          "=--,_                            
              ,-''    _  _       `,                        
             /   ,.-+(_)(_)�--.,   ;                       
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;                              
            !,'     ;   ;
            V'      ;   ;                                         
                    ;._.;                                        
                    ;   ;                                           
                    ;   ;        ~                               
     ~              ;._.;                                     
               ~    ;   ;                                            
                   .�   `.                ~                          
             __,.--;.___.;--.,___                         
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..
                  `                 ~
                              ~
             ~
             
             
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
      ''')

print("Welcome to The Treasure Island!")
print("Your mission is to find the treasure.")
print("You're at a crossroad! Which direction do you want to take?")
direction1 = input('Type "left" or "right". ').lower()


if direction1 == "right":
    print("Woops! You fell into a hole. Game is over.")
elif direction1 == "left":
   direction2 = input('You\'ve come to a lake. There is an island in the middle of the lake, Type "wait" to wait for a boat. Type "swim" to swim across. ')
   direction2 = direction2.lower()
   if direction2 == "swim":
       print("Storm is near! Game over.")
   elif direction2 == "wait":
       door = input('''Oh look, there's a house with 3 doors! Which one should we choose, the red,
             yellow or blue one? ''')
       if door == "red":
           print("You entered a room full of beasts. Game over.")
       elif door == "blue":
           print("You chose a room full of fire. Game over.")
       elif door == "yellow":
           print("You win Treasure Island!")
       else: 
           print("You chose a door that doesn't exist. Game over.")
   else:
       print("You got attacked by a grumpy monster! Game over.")
else: 
    print("You got attacked! Game over.")
