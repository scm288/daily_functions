from datetime import datetime


def tell_time():
    """Tells the current time."""
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    ts = datetime.timestamp(dt)

    print("\nDate and time is:", dt)
    print("Timestamp is:", ts, "\n")


def time_loop():
    """Give users the choice to get the time or quit."""
    wants_time = True
    print("Would you like the current time?")
    while wants_time:
        user_choice = input(
            "Enter [1] for the current time and [2] to quit. ")
        if user_choice == '1':
            wants_time = True
            tell_time()
            continue
        elif user_choice == '2':
            wants_time = False
            break
        else:
            print(
                "\nI'm sorry, I didn't get that.")
            continue


time_loop()

# Create a loop to tell the time over and over again.


# from datetime import datetime
# from datetime import timedelta


# class MountainTime(datetime.tzinfo):
#     """A subclass of datetime.tzinfo."""

#     def __init__(self):
#         super().__init__()


# # Calculate difference between Mountain Time Zone and UTC.
# mtz_delta = timedelta(hours=-7)

# # Input difference into datetime to calculate current timestamp.
# mtz = datetime.tzinfo(mtz_delta)


# def tell_time(time_zone):
#     """Tells the current time when run."""

#     # Fetch the current time.
#     current_time = datetime.now(time_zone)

#     # Print the current time every five seconds.
#     print(f"The current time is {current_time}")


# mtz_info = datetime.tzinfo()
# mtz = MountainTime(mtz_info)
# tell_time(mtz)

# This was my first attempt. I tried to calculate everything myself; my initial research told me that Python calculated everything according to UTC. However, an online tutorial supplied the above code, and by implementing it I saw that Python's datetime.now() already accounted for differences between local time and UTC. So I was doing redundant work.

# Lesson learned: always implement the simplest solution. If something says that it provides the right answer, give that a try instead of trying to rebuild the entire language yourself. Don't try to do everything on your own.

# What I was digging into: the simple tutorial mentioned datetime.now(). Instead of simply implementing this, I decided to track down the docs for that function and make it work myself. This led me to grapple with issues of class, subclass, abstract base classes (in the case of datetime.tzinfo), and so on--instead of printing the current time and date, as I wanted to.

# On a side note, I also managed to figure out how to close a user loop (which had been pestering me on an earlier experiment) without it being too janky. I tried nesting the user loop (putting an instance of the user loop function inside of the user loop function), but I found that you would then have to quit twice when you wanted to quit--not what I wanted! I learned how to use the step=by=step debugging console to figure this out. That will come in handy in the future.
