import random

# Four users, each with five pets
users = 5
pets = 3
user_names = ('Julie', 'Spencer', 'David', 'Angela', 'Johnson')
pet_names = ('Snookums', 'Harvey', 'Whiskers', 'Fluffy', 'Truman', 'Curly',
             'Elvis', 'Sammy', 'Max', 'Calvin', 'Hobbes', 'Luna', 'Toby', 'Desi', 'Kal')
chosen_names = []


def choose_name():
    """Chooses a pet name from the list. If already chosen, chooses another."""
    name_chosen = False
    while not name_chosen:
        choice = random.choice(pet_names)
        if choice in chosen_names:
            continue
        else:
            chosen_names.append(choice)
            name_chosen = True
    return choice


# Assign five pets for each of the four users
# Make sure that the right variable is being multiplied!
pets_per_user = [[''] * pets for i in range(users)]

for i in range(users):
    for j in range(pets):
        pets_per_user[i][j] = str(choose_name())

# Print off a report of who has what pet
for i in pets_per_user:
    user = pets_per_user.index(i)
    print(f"{user_names[user]}'s Pets: ", i)

# Trying to equate the index of i with the index of the current user_name
