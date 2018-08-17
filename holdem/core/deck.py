import itertools
import random
from dataclasses import dataclass
from typing import List, Tuple

from .cards import Card, Rank, Suit


@dataclass
class Deck:
    cards: List[Card]
    community_cards: List[Card]


def init() -> Deck:
    return Deck(
        [
            Card(r, s) for r, s in itertools.product(Rank, Suit)
            if r != Rank.one_ace
        ],
        []
    )


def shuffle(d: Deck) -> Deck:
    cards = d.cards[:]
    random.shuffle(cards)
    return Deck(cards, d.community_cards)


def draw(d: Deck) -> Tuple[Card, Deck]:
    cards = d.cards[:]
    c = cards.pop()
    return c, Deck(cards, d.community_cards)


def flop(d: Deck) -> Deck:
    c, d = draw(d)
    return Deck(d.cards, d.community_cards + [c])
