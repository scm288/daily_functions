def comparator(a, b):
    """Compares two values and returns a string result stating the outcome."""
    if a > b:
        return "greater than"
    elif a < b:
        return "less than"
    elif a == b:
        return "equal to"


print(comparator(3, -2))


class Comparator():
    """Contains methods that compare two values."""

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def is_greater_than(self):
        """Returns True if the first value is greater than the second value."""
        if self.a > self.b:
            return True
        else:
            return False

    def is_less_than(self):
        """Returns True if the first value is less than the second value."""
        if self.a < self.b:
            return True
        else:
            return False

    def is_equal_to(self):
        """Returns True if the first value is equal to the second value."""
        if self.a == self.b:
            return True
        else:
            return False


answer_1 = input("Please enter a number: ")
answer_2 = input("Please enter another number: ")

answer_comp = Comparator(int(answer_1), int(answer_2))

found_relationship = False
while found_relationship == False:
    answer = ""
    if answer_comp.is_greater_than() == True:
        answer = f"{answer_comp.a} is greater than {answer_comp.b}"
        found_relationship = True
    elif answer_comp.is_less_than() == True:
        answer = f"{answer_comp.a} is less than {answer_comp.b}"
        found_relationship = True
    elif answer_comp.is_equal_to() == True:
        answer = f"{answer_comp.a} is equal to {answer_comp.b}"
        found_relationship = True

print(answer)

# Lesson learned -- don't forget to call functions using parentheses!!
