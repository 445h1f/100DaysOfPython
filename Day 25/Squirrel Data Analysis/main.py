import pandas


data = pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
gray_color_counts = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_color_counts = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_color_counts = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_color_counts, cinnamon_color_counts, black_color_counts]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv('squirrel_fur_color_count_data.csv')

    
