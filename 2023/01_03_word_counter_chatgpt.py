from operator import itemgetter


def count_words(words):
    # Create an empty list to store the dictionaries
    word_counts = []

    # Iterate through the list of words
    for word in words:
        # Check if the word is already in the list of dictionaries
        found = False
        for d in word_counts:
            if d['name'] == word:
                # If the word is already in the list, add 1 to its count
                d['count'] += 1
                found = True
                break
        # If the word is not in the list, add a new dictionary with a count of 1
        if not found:
            word_counts.append({'name': word, 'count': 1})

    return word_counts


# Test the function
word_list = []
with open("2023_data/dc_ch_1.txt") as reader:
    for line in reader:
        for word in line.split():
            word_list.append(word)

# MAKE SURE THAT FUNCTION RESULTS ARE ASSIGNED TO VARIABLES LOL
counted_list = count_words(word_list)

# for item in counted_list:
#     if item['count'] == False:
#         item.pop()

sorted_list = sorted(counted_list, key=lambda x: x['count'], reverse=True)
print(sorted_list)

# This solution was created by ChatGPT. After busting my brain trying to figure this problem out on my own, I ended up turning to the AI to see what it would do. And what do you know? It is elegant, persuasive, and succinct.

# Amazing. It really is amazing what happens when you just, I don't know, fix that one error that has brought down the entire machine. And what an error! I just learned that merely calling a function does nothing, especially if the returned result isn't assigned to any sort of variable. No wonder my sorting code wasn't doing anything! The count_words() function call didn't get utilized or called upon at all!

# But fixing that--that one thing--made the result possible, something I'd slaved over for the past couple of days. And now I did it. And I danced and jumped up and down, ecstatically. There is no rush quite like figuring something out.

# Man. I could get used to this feeling.
