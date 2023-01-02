# with open('2023_data/dc_ch_1.txt', 'r') as reader:
#     # Read and print the entire file line by line
#     print(type(reader))
#     # line = reader.readline()
#     # while line != '':  # The EOF char is an empty string
#     #     print(line, end='')
#     #     line = reader.readline()

word_counter = []

reader = ['this this this is is is a a a sample sample sample list list list']

for line in reader:
    for word in line.split():
        if word_counter == []:
            word_entry = {
                'word_name': word,
                'count': 1,
            }
            word_counter.append(word_entry)
        else:
            for entry in word_counter:
                if entry['word_name'] == word:
                    entry['count'] += 1
                elif entry['word_name'] != word:

                    # if entry['word_name'] == word not in word_counter:
                    #     print(f"The entry '{entry['word_name']}' is not in the list")
                    #         else:
                    #             for entry in word_counter:
                    #                 if entry['word_name'] == word:
                    #                     entry['count'] += 1
                    #                 elif entry['word_name'] != word:
                    #                     continue
                    #             if entry['word_name'] == word not in word_counter:
                    #                 print(f"The entry '{entry['word_name']}' is not in the list")
                    #                 word_entry = {
                    #                     'word_name': word,
                    #                     'count': 1,
                    #                 }
                    #                 word_counter.append(word_entry)
                    # print(word_counter)

                    # word_entry = {
                    #     'word_name': word,
                    #     'count': 1
                    # }
                    # if

                    # if word_entry not in word_counter:
                    #     word_counter.append(word_entry)
                    # elif word_entry in word_counter:
                    #     temp_value = word_entry[f'{word}']
                    #     temp_value += 1
                    #     word_entry[f'{word}'] = temp_value
                    #     for entry in word_counter:
                    #         if str(word_entry.keys()) in entry.keys():
                    #             word_counter[f'{word}'] = word_entry
                    #     print(word_entry[f'{word}'])

                    # for line in reader:
                    #     for word in line.split():
                    #         if word_counter == []:
                    #             word_entry = {
                    #                 word: 0
                    #             }
                    #             word_counter.append(word_entry)
                    #         for entry in word_counter:
                    #             if word not in word_counter.keys():
                    #                 word_entry = {
                    #                     word: 1
                    #                 }
                    #             elif word in word_counter.keys():
                    #                 word_counter[f'{word}'] += 1
