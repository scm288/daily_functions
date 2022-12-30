import random

deleted_items = []


def Popper(popped, list=[]):
    """Removes the specified element from a list."""
    sample_slice = list[popped]
    deleted_items.append(sample_slice)
    list.pop(popped)
    print(sample_slice)
    print(list)
    print(deleted_items)


def Sequencer(list=[]):
    """Iterates through a list one item at a time."""
    """Removes the items in the list before its current position."""
    """Stores deleted items in a list."""
    print(f"\nDeleted items: {deleted_items}")
    print(f"The current item is {list[0]['name']}")
    deleted_items.append(list[0])
    list.pop(0)
    print(f"Remaining items are {list}")


def Reshuffler(deletion_list, list=[], times=1):
    """Reshuffles a deleted item back into the list a number of times."""
    print(f"Deleted items, pre-shuffle: {deleted_items}")
    for t in range(times):
        list.append(deletion_list[0])
    deletion_list.pop(0)
    random.shuffle(list)
    print(f"The list is currently in this order: {list}")
    print(f"Deleted items, post-shuffle: {deleted_items}")


sample_list = []
for i in range(10):
    new_dict = {
        'name': f"Thing {i+1}",
    }
    sample_list.append(new_dict)

# Sequencer(sample_list)
# Reshuffler(deleted_items, sample_list, 3)
Popper(-1, sample_list)
