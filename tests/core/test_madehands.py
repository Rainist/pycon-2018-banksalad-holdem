import unittest

import holdem.core.madehands as m
from holdem.core.cards import Card, Rank, Suit


class TestMadeHands(unittest.TestCase):

    def test_evaluate(self):
        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ace, Suit.heart),
                    Card(Rank.two, Suit.heart),
                    Card(Rank.three, Suit.heart),
                    Card(Rank.four, Suit.heart),
                    Card(Rank.five, Suit.heart),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.seven, Suit.heart)
                ]
            ),
            m.MadeHands.straight_flush
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ace, Suit.heart),
                    Card(Rank.ace, Suit.club),
                    Card(Rank.ace, Suit.diamond),
                    Card(Rank.ace, Suit.spade),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.seven, Suit.diamond),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.four_card
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.ten, Suit.heart),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.six, Suit.club),
                    Card(Rank.eight, Suit.spade),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.full_house
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ace, Suit.spade),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.two, Suit.spade),
                    Card(Rank.eight, Suit.spade),
                    Card(Rank.king, Suit.spade),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.flush
        )

        # todo: straight case error!
        # self.assertEqual(
        #     m.evaluate(
        #         [
        #             Card(Rank.ten, Suit.spade),
        #             Card(Rank.nine, Suit.heart),
        #             Card(Rank.eight, Suit.spade),
        #             Card(Rank.seven, Suit.club),
        #             Card(Rank.six, Suit.heart),
        #             Card(Rank.eight, Suit.spade),
        #             Card(Rank.two, Suit.heart)
        #         ]
        #     ),
        #     m.MadeHands.straight
        # )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.ten, Suit.heart),
                    Card(Rank.ten, Suit.diamond),
                    Card(Rank.seven, Suit.club),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.eight, Suit.spade),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.triple
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ace, Suit.spade),
                    Card(Rank.ten, Suit.heart),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.eight, Suit.club),
                    Card(Rank.eight, Suit.spade),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.two_pair
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.ace, Suit.spade),
                    Card(Rank.ten, Suit.heart),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.eight, Suit.club),
                    Card(Rank.king, Suit.spade),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.two, Suit.heart)
                ]
            ),
            m.MadeHands.one_pair
        )

        self.assertEqual(
            m.evaluate(
                [
                    Card(Rank.two, Suit.spade),
                    Card(Rank.jack, Suit.heart),
                    Card(Rank.ten, Suit.spade),
                    Card(Rank.eight, Suit.club),
                    Card(Rank.king, Suit.spade),
                    Card(Rank.six, Suit.heart),
                    Card(Rank.three, Suit.heart)
                ]
            ),
            m.MadeHands.top
        )


if __name__ == '__main__':
    unittest.main()
