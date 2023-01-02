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

word_list = []
word_counter = []

with open('2023_data/dc_ch_1.txt', 'r') as reader:
    # Read and print the entire file line by line
    # line = reader.readline()
    # while line != '':  # The EOF char is an empty string
    #     print(line, end='')
    #     line = reader.readline()
    for line in reader:
        for word in line.split():
            word_entry = {
                word: 1
            }
            if word_entry not in word_counter:
                word_counter.append(word_entry)
            elif word_entry in word_counter:
                temp_value = word_entry[f'{word}']
                temp_value += 1
                word_entry[f'{word}'] = temp_value
                print(word_entry[f'{word}'])


# This is a sample bit of code from the internet. Wow. That works perfectly. It seems that the function/method I was looking for was readline(), which is called on an opened .txt file. And, on top of that, line.split() breaks it up into individual words! Aha! Exactly what I was looking for! Now to read up on that .split() method...