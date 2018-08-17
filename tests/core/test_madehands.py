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

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.two, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.heart),
                    Card(Rank.four, Suit.spade),
                    Card(Rank.eight, Suit.heart),
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
                    Card(Rank.two, Suit.heart)
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

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.jack, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.club),
                    Card(Rank.jack, Suit.diamond),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.four_of_a_kind, Rank.jack)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.jack, Suit.heart)
                ],
                [
                    Card(Rank.jack, Suit.club),
                    Card(Rank.three, Suit.diamond),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.full_house, Rank.jack)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.two, Suit.heart)
                ],
                [
                    Card(Rank.ace, Suit.club),
                    Card(Rank.four, Suit.diamond),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.straight, Rank.six)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.two, Suit.spade)
                ],
                [
                    Card(Rank.ace, Suit.spade),
                    Card(Rank.four, Suit.spade),
                    Card(Rank.eight, Suit.spade),
                    Card(Rank.five, Suit.spade),
                    Card(Rank.six, Suit.heart)
                ]
            ),
            (MadeHands.flush, Rank.jack)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.spade),
                    Card(Rank.two, Suit.club)
                ],
                [
                    Card(Rank.ace, Suit.club),
                    Card(Rank.four, Suit.club),
                    Card(Rank.three, Suit.club),
                    Card(Rank.five, Suit.club),
                    Card(Rank.six, Suit.club)
                ]
            ),
            (MadeHands.straight_flush, Rank.six)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.club),
                    Card(Rank.two, Suit.club)
                ],
                [
                    Card(Rank.nine, Suit.club),
                    Card(Rank.king, Suit.club),
                    Card(Rank.queen, Suit.club),
                    Card(Rank.ten, Suit.club),
                    Card(Rank.six, Suit.club)
                ]
            ),
            (MadeHands.straight_flush, Rank.king)
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.jack, Suit.club),
                    Card(Rank.two, Suit.club)
                ],
                [
                    Card(Rank.ace, Suit.club),
                    Card(Rank.king, Suit.club),
                    Card(Rank.queen, Suit.club),
                    Card(Rank.ten, Suit.club),
                    Card(Rank.six, Suit.club)
                ]
            ),
            (MadeHands.royal_flush, Rank.ace)
        )


if __name__ == '__main__':
    unittest.main()
