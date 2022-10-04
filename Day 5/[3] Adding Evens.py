#Write your code below this row 👇

sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum += number

print(sum)

# or
sum2 = 0
for number in range(2, 101, 2):
    sum2 += number

print(sum2)