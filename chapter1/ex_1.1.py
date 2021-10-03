import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()

    # len use magin method __len__ of Deck class
    print(len(deck))

    # __getitem__ magic method works
    print(deck[0])

    # __getitem__ magic method
    print(choice(deck))

    print(deck[12::13])

    # 'in' works when __contains__ is not implemented.
    # we can iterate deck, since there is __getitem__ method. So, in makes an iteration for deck, and find for Card
    print(Card('3', 'hearts') in deck)

    # deck has __getitem__, so deck acts like a standard python sequence.
    for card in sorted(deck, key=spades_high):
        print(card)
