list = [1, 2, 3, 4, 5, 6]
list_segment = []

for item in list:
    if len(list_segment) < 2:
        list_segment.append(item)
    else:
        list_segment = []
        list_segment.append(item)
    if len(list_segment) == 2:
        print(list_segment)
