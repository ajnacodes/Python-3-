# Average Height Calculator
# insert some heights and it will calculate the average height
# eg: 175 168 180 184
student_heights = input("Input a list of student heights ").split()
# loop for converting each input into int
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# solution:
# one way of doing this is: 
#  total_height = sum(student_heights)
#  number_of_students = len(student_heights)
#  average_height = total_height / number_of_students
#  print(average_height)
total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

