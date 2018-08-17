import unittest

import holdem.core.madehands as m
from holdem.core.cards import Card, Rank, Suit
from holdem.core.madehands import MadeHands


class TestMadeHands(unittest.TestCase):

    def test_evaluate(self):
        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.three, Suit.heart),
                    Card(Rank.two, Suit.heart)
                ],
                [
                    Card(Rank.ace, Suit.heart),
                    Card(Rank.four, Suit.heart),
                    Card(Rank.five, Suit.heart),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.seven, Suit.heart)
                ]
            ),
            (MadeHands.straight_flush, Rank.seven)
        )
