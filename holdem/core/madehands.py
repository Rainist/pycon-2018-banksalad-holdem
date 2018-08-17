from .cards import Card, Rank, Suit
from enum import IntEnum
from typing import List, Optional, Tuple
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


def _is_straight(cards: List[Card]) -> bool:
    cards = cards[:]

    if cards[-1].rank == Rank.ace:
        cards = [1] + cards

    for i in range(0, 4):
        card_slice = cards[i + 5 : i : -1]
        if all(x.rank - y.rank == 1 for x, y in zip(card_slice, card_slice[1:])):
            return True

    return False


def evaluate(user_cards: List[Card], community_cards: List[Card]) -> Tuple[MadeHands, int]:
    cards = (user_cards + community_cards)
    cards.sort(key=lambda card: (card.rank, card.suit))

    rank_grouped_cards = [list(v) for _, v in groupby(cards, key=lambda c: c.rank)]
    rank_grouped_cards = {
        #flatten = list(chain.from_iterable(list(v)))
        #flatten.sort(key=lambda card: card.rank)
        k : list(chain.from_iterable(list(v)))
        for k, v in groupby(rank_grouped_cards, key=lambda cs: len(cs))
    }

    suit_grouped_cards = [
        list(v)#.sort(key=lambda card: card.rank)
        for _, v in groupby(cards, key=lambda c: c.suit)
    ]
    suit_grouped_cards = {
        len(suit) : suit for suit in suit_grouped_cards
    }
    rsfcs = cards[2:]

    if map(lambda c: c.rank, rsfcs) == STRAIGHT_FLUSH_RANKS and _is_same_suit(rsfcs):
        return (
            MadeHands.royal_flush,
            rsfcs[-1].suit
        )
    elif 5 in suit_grouped_cards and suit_grouped_cards[5] and _is_straight(suit_grouped_cards[5]):
        return (
            MadeHands.straight_flush,
            suit_grouped_cards[5][-1].rank
        )
    elif 4 in rank_grouped_cards and rank_grouped_cards[4]:
        return (
            MadeHands.four_of_a_kind,
            rank_grouped_cards[4][-1].rank
        )
    elif 2 in rank_grouped_cards and 3 in rank_grouped_cards and rank_grouped_cards[2] and rank_grouped_cards[3]:
        return (
            MadeHands.full_house,
            rank_grouped_cards[3][-1].rank
        )
    elif 5 in suit_grouped_cards and _is_same_suit(suit_grouped_cards[5]):
        return (
            MadeHands.flush,
            suit_grouped_cards[-1].rank
        )
    elif _is_straight(cards):
        return (
            MadeHands.straight,
            Rank.ace if (cards[0].rank == Rank.ace) else cards[-1].rank
        )
    elif 3 in rank_grouped_cards and rank_grouped_cards[3]:
        return (MadeHands.three_of_kind, rank_grouped_cards[3][-1].rank)
    elif 2 in rank_grouped_cards and len(rank_grouped_cards[2]) == 4:
        return (MadeHands.two_pairs, rank_grouped_cards[2][-1].rank)
    elif 2 in rank_grouped_cards and rank_grouped_cards[2]:
        return (MadeHands.pair, rank_grouped_cards[2][-1].rank)
    else:
        return (MadeHands.high_card, _get_high_card_weight(user_cards))
