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

# Wow, what a learning experience! And what an awesome learning curve. This morning, I did several things:

# 1. I figured out how to install git onto my aging Macbook Air. (No small feat, given that the Macbook is so old that it can't be updated to the latest OS; and XCode requires the current OS. So I had to get creative.)

# 2. Figuring out, with my own unique git setup, how to connect to Github.

# 3. Figuring out how to clone repositories (in this case, my daily_functions folder, since I'm on a different computer).

# 4. Figuring out nested arrays! I've seen these things several times before, and I wanted to tackle them head-on. So I did it. I was confused for the longest time. I thought that in a given array (nested_array = [A][B]), that A would have a value of its own, but no--it really is just an identifier for the nested values within it. It's not a folder, or a tabulation like a JSON dictionary. It doesn't have a name or identifier assigned to it. If I want to do something like that, I'll probably need to set up a dictionary instead. No, that's just a number that determines which nested element I'm referring to. Once I figured that out, I realized that trying to assign values to that number, [A], was fruitless. So I stopped doing that and reworked my design, and I got it done!

# Amazing what happens when you learn how things actually work. Onward!

# 5. It helps when you don't accidentally proc a silent "exceed range" error by having more slots for variables in your list ("slots for pet names") than you do variables ("pet names"). Make sure the two line up!
