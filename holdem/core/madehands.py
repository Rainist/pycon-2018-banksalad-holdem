from .cards import Card, Rank, Suit
from enum import IntEnum
from typing import List, Tuple
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


def _get_card_rank(card: Card):
    return card.rank


def _get_tuple_of_card_rank_and_suit(card: Card):
    return card.rank, card.suit


def _get_high_card_weight(cards: List[Card]) -> Rank:
    return max(cards, key=_get_card_rank).rank


def _is_same_suit(cards: List[Card]) -> bool:
    return all(cards[0].suit == card.suit for card in cards)


def _get_straight_cards(cards: List[Card]) -> List[Card]:
    circulated_cards = [Card(Rank.one_ace, cards[-1].suit)] + cards \
        if cards[-1].rank == Rank.ace else cards

    for i in range(0, 4):
        card_slice = circulated_cards[-1 - i: -6 - i: -1]
        if all(
            x.rank - y.rank == 1 for x, y in zip(card_slice, card_slice[1:])
        ):
            return card_slice

    return []


def _get_flush_cards(cards: List[Card]) -> List[Card]:
    card_suits = [card.suit for card in cards]
    for suit in Suit:
        if card_suits.count(suit) >= 5:
            return sorted(
                [card for card in cards if card.suit == suit],
                key=_get_card_rank
            )[:5]

    return []


def evaluate(
    user_cards: List[Card], community_cards: List[Card]
) -> Tuple[MadeHands, Rank]:
    hand_cards = sorted(
        (user_cards + community_cards),
        key=_get_tuple_of_card_rank_and_suit
    )

    rank_grouped_cards = sorted([
        list(v) for _, v in groupby(hand_cards, key=_get_card_rank)
    ], key=len)

    card_pairs = {
        k: list(chain.from_iterable(list(v)))
        for k, v in groupby(rank_grouped_cards, key=len)
    }

    highest_cards = hand_cards[2:]

    straight_mate = _get_straight_cards(hand_cards)
    flush_mate = _get_flush_cards(hand_cards)
    straight_flush_mate = _get_flush_cards(straight_mate)

    if straight_flush_mate and straight_flush_mate[-1].rank == Rank.ace:
        return (
            MadeHands.royal_flush,
            highest_cards[-1].rank
        )
    elif straight_flush_mate:
        return (
            MadeHands.straight_flush,
            straight_flush_mate[-1].rank
        )
    elif 4 in card_pairs:
        return (
            MadeHands.four_of_a_kind,
            card_pairs[4][-1].rank
        )
    elif 2 in card_pairs and 3 in card_pairs:
        return (
            MadeHands.full_house,
            card_pairs[3][-1].rank
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
    elif 3 in card_pairs:
        return MadeHands.three_of_kind, card_pairs[3][-1].rank
    elif 2 in card_pairs and len(card_pairs[2]) >= 4:
        return MadeHands.two_pairs, card_pairs[2][-1].rank
    elif 2 in card_pairs:
        return MadeHands.pair, card_pairs[2][-1].rank
    else:
        return MadeHands.high_card, _get_high_card_weight(hand_cards)
