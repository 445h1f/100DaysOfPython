with open('file1.txt') as file1:
    file1_data= file1.readlines()
    file1_numbers = [int(n.strip()) for n in file1_data]

with open('file2.txt') as file2:
    file2_data = file2.readlines()
    file2_numbers = [int(n.strip()) for n in file2_data]

result = [int(num) for num in file1_numbers if num in file2_numbers]

print(result)