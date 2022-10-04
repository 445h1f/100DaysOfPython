# with open('weather_data.csv') as data_file:
#     data = file.readline()
#     print(data)



# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temp = int(row[1])
#             temperatures.append(temp)

import pandas

data = pandas.read_csv('weather_data.csv')

# temperatures = data['temp'].to_list()


# avg_temp = sum(temperatures) / len(temperatures)

# print(f'Average Temperture was {avg_temp}')

# get data in columns
# print(data['temp'].mean())
# print(data['temp'].max())

# get data in rows
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])


# get data from of any col in row

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)

# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)

# create pandas dataframe from scratch

data_dict = {
    'students' : ['John', 'Joe', 'Jamie', 'Jack'],
    'marks' : [8, 9, 10, 7]
} 

new_data = pandas.DataFrame(data_dict) # converts dict to pandas dataframe object

# exporting to csv file
new_data.to_csv('new_data.csv')
