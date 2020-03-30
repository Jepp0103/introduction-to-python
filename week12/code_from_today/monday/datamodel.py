# datamode.py


class A:
    
    def __init__(self):
        self.name = 'Claus'

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.name + other.name



class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __getitem__(self, key):
        return self.cards[key]
