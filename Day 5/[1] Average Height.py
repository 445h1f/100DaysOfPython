# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

numHeights = len(student_heights)

sumHeights = 0

for height in student_heights:
    sumHeights += height

avgHeight = round(sumHeights / numHeights)

print(avgHeight)