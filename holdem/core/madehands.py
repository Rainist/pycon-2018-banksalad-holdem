from .cards import Card, Rank, Suit
from enum import IntEnum
from typing import List, Optional, Tuple
from itertools import groupby


TRIPLE_LENGTH = 3
FOUR_CARD_LENGTH = 4
FLUSH_LENGTH_THRESHOLD = 5
ROYALE_STRAIGHT_FLUSH_RANKS = [Rank.ace, Rank.ten, Rank.jack, Rank.queen, Rank.king]
BACK_STRAIGHT_FLUSH_RANKS = [Rank.ace, Rank.two, Rank.three, Rank.four, Rank.five]
MOUNTAIN_RANKS = ROYALE_STRAIGHT_FLUSH_RANKS


class MadeHands(IntEnum):
    top = 1
    one_pair = 2
    two_pair = 3
    triple = 4
    straight = 5
    back_straight = 6
    mountain = 7
    flush = 8
    full_house = 9
    four_card = 10
    straight_flush = 11
    back_straight_flush = 12
    royale_straight_flush = 13


def evaluate(cards: List[Card]) -> Tuple[MadeHands, Rank, Suit]:
    cards = cards[:]
    cards.sort(key=lambda c: (c.suit, c.rank))

    suits = [list(v) for _, v in groupby(cards, key=lambda c: c.suit)]
    suit_dict = {
        len(suit) : suit for suit in suits
    }
    longest_suit = suit_dict[max(suit_dict)]

    if (len(longest_suit) == FLUSH_LENGTH_THRESHOLD):
        suit = longest_suit[0].suit
        suits = list(map(lambda x: x.rank, longest_suit))
        max_rank = longest_suit[4].rank
        if (suits == ROYALE_STRAIGHT_FLUSH_RANKS):
            return (MadeHands.royale_straight_flush, Rank.ace, suit)
        elif (suits == BACK_STRAIGHT_FLUSH_RANKS):
            return (MadeHands.back_straight_flush, Rank.ace, suit)
        elif (all(y - x == 1 for x, y in zip(suits, suits[1:]))):
            return (MadeHands.straight_flush, suit, max_rank)
        else:
            return (MadeHands.flush, suit, max_rank)
    else:
        pass # TODO
