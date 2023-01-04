list_of_dicts = [{'name': 'Alice', 'age': 25},    {
    'name': 'Bob', 'age': 30},    {'name': 'Eve', 'age': 20},]
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'], reverse=True)
print(sorted_list)
