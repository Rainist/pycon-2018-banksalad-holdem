import unittest

import holdem.core.madehands as m
from holdem.core.cards import Card, Rank, Suit
from holdem.core.madehands import MadeHands


class TestMadeHands(unittest.TestCase):

    def test_evaluate(self):
        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.two, Suit.club),
                    Card(Rank.two, Suit.heart)
                ],
                [
                    Card(Rank.ace, Suit.heart),
                    Card(Rank.ace, Suit.club),
                    Card(Rank.five, Suit.heart),
                    Card(Rank.six, Suit.club),
                    Card(Rank.seven, Suit.heart)
                ]
            ),
            (MadeHands.straight_flush, Rank.seven)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.two, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.heart),
                    Card(Rank.four, Suit.spade),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.pair, Rank.jack)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.five, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.heart),
                    Card(Rank.four, Suit.spade),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.two_pairs, Rank.jack)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.five, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.heart),
                    Card(Rank.jack, Suit.diamond),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.three_of_kind, Rank.jack)
        )


if __name__ == '__main__':
    unittest.main()
