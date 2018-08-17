from dataclasses import dataclass
from enum import IntEnum


class Suit(IntEnum):
    club = 1
    heart = 2
    diamond = 3
    spade = 4


class Rank(IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


@dataclass(repr=False, frozen=True)
class Card:
    rank: Rank
    suit: Suit

    def __repr__(self):
        return f'{self.rank.name} of {self.suit.name}s'
