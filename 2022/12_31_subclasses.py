import random


class Card:
    """Creates an instance of a card with a point value."""

    def __init__(self, points):
        self.points = str(points)


class SuiteCard(Card):
    """A subclass of Card that assigns a suite and color."""

    def __init__(self, points, suite=0):
        """Initializes values of the card and assigns a suite/color."""
        super().__init__(points)
        self.suite = self._assign_suite(suite)
        self.name = self._assign_name(self.points)

    def _assign_suite(self, suite=0):
        """Assigns the suite/color of the card."""
        if suite == 1:
            self.color = 'black'
            self.assigned_suite = 'clubs'
        elif suite == 2:
            self.color = 'black'
            self.assigned_suite = 'spades'
        elif suite == 3:
            self.color = 'red'
            self.assigned_suite = 'hearts'
        elif suite == 4:
            self.color = 'red'
            self.assigned_suite = 'diamonds'

    def _assign_name(self, points):
        """Depending on the point value, assign a name to the card."""
        if self.points == '1':
            return 'ace'
        elif self.points == '11':
            return 'jack'
        elif self.points == '12':
            return 'queen'
        elif self.points == '13':
            return 'king'
        else:
            return None


deck = []
for suite in range(4):
    for card in range(13):
        new_card = SuiteCard(card+1, suite+1)
        deck.append(new_card)

# for card in deck:
#     print(f"Points: {card.points}")
#     print(f"Color:  {card.color}")
#     print(f"Suite:  {card.assigned_suite}\n")

for card in deck:
    print(f"{card.points, card.color, card.assigned_suite, card.name}")

random.shuffle(deck)

for card in deck:
    print(f"{card.points, card.color, card.assigned_suite, card.name}")
