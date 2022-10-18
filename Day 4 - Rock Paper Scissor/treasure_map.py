# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# slicing postion to get row and column
row = int(position[0])
column = int(position[1])

# selcting row 
selectedRow = map[row-1]

# placing treasure
selectedRow[column-1] = 'x'

print(f'{map[0]}\n{map[1]}\n{map[2]}')  







#Write your code above this row 👆