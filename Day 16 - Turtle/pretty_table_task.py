import prettytable

table = prettytable.PrettyTable()

table.field_names = ['Name', 'Age', 'Country', 'Email', 'Premium']
table.title = 'UserData'
table.add_row(['Jake', 18, 'United Kingdom', 'jake@domaim.com', False])
table.add_row(['Rhea', 20, 'India', 'rhea@domain.com', True])

print(table)
