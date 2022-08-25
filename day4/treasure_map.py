# Treasure Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# first digit is the column, second digit is the row eg:32

#Write your code below this row 👇
column = int(position[0])
row = int(position[1])
map[row -1][column -1] = "X"


print(f"{row1}\n{row2}\n{row3}")
