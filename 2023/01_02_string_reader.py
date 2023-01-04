# doc = open("2023_data/dc_ch_1.txt")

# It turns out that .txt files are already organized by line. What can I do with this as a result? I think I'm going to use what I did before, with the line parsing, and set an adjustable parameter to determine how long printed lines are

# line_length = 12
# doc_line = []

# for line in doc:
#     for word in line:
#         if len(doc_line) < line_length:
#             doc_line.append(word)
#         else:
#             doc_line = []
#             doc_line.append(word)
#         if len(doc_line) == line_length:
#             print(doc_line)

# It turns out that doc[line][word] is actually doc[line][character]--this format skips words entirely! Which I guess makes some sense; it's easier to count characters (including spaces and punctuation) than it is to quantify the limits of individual words, since those vary so much. Huh. How do I go about parsing words, then? Not sure...

# word_list = []
# word_counter = []

# with open('2023_data/dc_ch_1.txt', 'r') as reader:
#     # Read and print the entire file line by line
#     # line = reader.readline()
#     # while line != '':  # The EOF char is an empty string
#     #     print(line, end='')
#     #     line = reader.readline()
#     for line in reader:
#         for word in line.split():


# This is a sample bit of code from the internet. Wow. That works perfectly. It seems that the function/method I was looking for was readline(), which is called on an opened .txt file. And, on top of that, line.split() breaks it up into individual words! Aha! Exactly what I was looking for! Now to read up on that .split() method...

def get_values(list=[], key=''):
    result_list = []
    for dictionary in list:
        result_list.append(dictionary[key])
    return result_list


word_list = []
word_counter = []

# Read the document and split it into individual words. Make it into a list titled "word_list".
with open('2023_data/dc_ch_1.txt', 'r') as reader:
    for line in reader:
        for word in line.split():
            word_list.append(word)

for word in word_list:
    # For every word in word_list:
    # Find out what words are currently in word_counter.
    word_counter_results = get_values(word_counter, 'name')
    if word_counter == []:
        # If word_counter is empty, create the first entry.
        word_entry = {
            'name': word,
            'count': 1,
        }
        word_counter.append(word_entry)

    elif word in word_counter_results:
        # If the given word IS in word_counter_results:
        specified_entry = next(word_counter, {'name': word})

        # results = get_values(word_counter, 'name')
        # print(results)

        # result = [
        #     w for w in line.split() if w[0] == f'{word}' in word_counter]

        # exampleSet = [{'type': 'type1'}, {'type': 'type2'},
        #               {'type': 'type2'}, {'type': 'type3'}]
        # keyValList = ['type2', 'type3']
        # expectedResult = [d for d in exampleSet if d['type'] in keyValList]
        # print(expectedResult)
