from enum import IntEnum
from typing import Iterable, List

from .cards import Card


class MadeHands(IntEnum):
    top = 1
    one_pair = 2
    two_pair = 3
    triple = 4
    straight = 5
    flush = 8
    full_house = 9
    four_card = 10
    straight_flush = 11


def _is_straight(ranks: Iterable[int]) -> bool:
    sorted_ranks = sorted(ranks)
    return all(y - x == 1 for x, y in zip(sorted_ranks, sorted_ranks[1:]))


def evaluate(cards: List[Card]) -> int:
    suits = [c.suit for c in cards]

    flush_table = {
        min(suits.count(s), 5): _is_straight(c.rank for c in cards if c.suit == s)
        for s in suits
    }
    flush = 5 in flush_table

    ranks = [c.rank for c in cards]
    pairs = [ranks.count(r) for r in set(ranks)]

    if flush and flush_table[5]:
        return MadeHands.straight_flush
    elif 4 in pairs:
        return MadeHands.four_card
    elif 3 in pairs and 2 in pairs:
        return MadeHands.full_house
    elif flush:
        return MadeHands.flush
    elif _is_straight(c.rank for c in cards):
        return MadeHands.straight
    elif 3 in pairs:
        return MadeHands.triple
    elif pairs.count(2) >= 2:
        return MadeHands.two_pair
    elif 2 in pairs:
        return MadeHands.one_pair
    else:
        return MadeHands.top
