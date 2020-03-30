# deck_exercise.py
"""
Continue with the deck example and implement the

    __len__ method
    __add__ method
    __repr__ method
    __str__ method
    __setitem__ method
    __delitem__ method

"""

class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        d = Deck()
        d.cards.append(self.cards + other.cards)
        return d

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return str(self.cards)

    def __setitem__(self, key, val):
        self.cards[key] = val

    def __delitem__(self, key):
        del(self.cards[key])
