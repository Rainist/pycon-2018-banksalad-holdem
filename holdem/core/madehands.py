from .cards import Card, Rank, Suit
from collections import defaultdict
from enum import IntEnum
from typing import List, Optional, Tuple, Union
from itertools import chain, groupby


STRAIGHT_FLUSH_RANKS = [Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace]


class MadeHands(IntEnum):
    high_card = 1
    pair = 2
    two_pairs = 3
    three_of_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9
    royal_flush = 10


def _get_high_card_weight(cards: List[Card]) -> int:
    return max(cards, key=lambda card: card.rank)


def _is_same_suit(cards: List[Card]) -> bool:
    head = cards[0]
    tail = cards[1:]
    return all(head.suit == card.suit for card in tail)


def _get_straight_cards(cards: List[Card]) -> List[Card]:
    cards = cards[:]

    if cards[-1].rank == Rank.ace:
        cards = [Card(Rank.one_ace, cards[-1].suit)] + cards

    for i in range(2, -2, -1):
        card_slice = cards[i + 5: i: -1]
        if all(x.rank - y.rank == 1 for x, y in zip(card_slice, card_slice[1:])):
            return card_slice

    return []


def _get_flush_cards(cards: List[Card]) -> List[Card]:

    def _get_rank(card: Card):
        return card.rank

    card_suits = [card.suit for card in cards]
    for suit in Suit:
        if card_suits.count(suit) >= 5:
            return sorted([card for card in cards if card.suit == suit], key=_get_rank)[:5]

    return []


def evaluate(user_cards: List[Card], community_cards: List[Card]) -> Tuple[MadeHands, int]:
    cards = (user_cards + community_cards)
    cards.sort(key=lambda card: (card.rank, card.suit))

    default_grouped_cards = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None
    }

    rank_grouped_cards = [list(v) for _, v in groupby(cards, key=lambda c: c.rank)]
    rank_grouped_cards = default_grouped_cards.update({
        #flatten = list(chain.from_iterable(list(v)))
        #flatten.sort(key=lambda card: card.rank)
        k: list(chain.from_iterable(list(v)))
        for k, v in groupby(rank_grouped_cards, key=lambda cs: len(cs))
    })

    rsfcs = cards[2:]

    straight_mate = _get_straight_cards(cards)
    flush_mate = _get_flush_cards(cards)
    straight_flush_mate = _get_flush_cards(straight_mate)
    if map(lambda c: c.rank, rsfcs) == STRAIGHT_FLUSH_RANKS and _is_same_suit(rsfcs):
        return (
            MadeHands.royal_flush,
            rsfcs[-1].suit
        )
    elif straight_flush_mate:
        return (
            MadeHands.straight_flush,
            straight_flush_mate[-1].rank
        )
    elif rank_grouped_cards[4]:
        return (
            MadeHands.four_of_a_kind,
            rank_grouped_cards[4][-1].rank
        )
    elif rank_grouped_cards[2] and rank_grouped_cards[3]:
        return (
            MadeHands.full_house,
            rank_grouped_cards[3][-1].rank
        )
    elif flush_mate:
        return (
            MadeHands.flush,
            flush_mate[-1].rank
        )
    elif straight_mate:
        return (
            MadeHands.straight,
            straight_mate[0].rank
        )
    elif rank_grouped_cards[3]:
        return MadeHands.three_of_kind, rank_grouped_cards[3][-1].rank
    elif len(rank_grouped_cards[2]) >= 4:
        return MadeHands.two_pairs, rank_grouped_cards[2][-1].rank
    elif rank_grouped_cards[2]:
        return MadeHands.pair, rank_grouped_cards[2][-1].rank
    else:
        return MadeHands.high_card, _get_high_card_weight(user_cards)
