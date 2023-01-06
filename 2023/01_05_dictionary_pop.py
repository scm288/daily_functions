def dictionary_pop(minimum, list=[]):
    """Iterates through a list of dictionaries. If the designated minimum threshold value isn't met, .pop() the dictionary from the list. Then return the curated list."""

    for item in list:
        if item['count'] == minimum:
            list.pop(item)

    return list


with open("2023_data/text_output_test.txt") as text:
    read_text = text.read()
    formatted_text = read_text.replace('}', '')
    formatted_text = formatted_text.replace('{', '')
    formatted_text = formatted_text.replace('name', '\n\'name')
    formatted_text = formatted_text.replace('unt\': ')
    print(formatted_text)

    # text_list = list(text.split())
    # print(text_list[1])

# curated_list = dictionary_pop(1, text)

# print(curated_list)

# with open("2023_data/test.txt") as test:
#     test = test.read()
#     print(test)
