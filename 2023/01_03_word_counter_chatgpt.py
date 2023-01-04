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

count_words(word_list)

sorted_list = sorted(word_list, key=itemgetter(1), reverse=True)
print(sorted_list)

# This solution was created by ChatGPT. After busting my brain trying to figure this problem out on my own, I ended up turning to the AI to see what it would do. And what do you know? It is elegant, persuasive, and succinct.
