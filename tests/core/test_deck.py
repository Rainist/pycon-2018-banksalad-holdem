import unittest

import holdem.core.deck as d
from holdem.core.cards import Card, Rank, Suit


class TestDeck(unittest.TestCase):

    def test_init(self):
        deck = d.init()
        self.assertListEqual(
            deck.cards,
            [
                Card(Rank.ace, Suit.club),
                Card(Rank.ace, Suit.heart),
                Card(Rank.ace, Suit.diamond),
                Card(Rank.ace, Suit.spade),
                Card(Rank.two, Suit.club),
                Card(Rank.two, Suit.heart),
                Card(Rank.two, Suit.diamond),
                Card(Rank.two, Suit.spade),
                Card(Rank.three, Suit.club),
                Card(Rank.three, Suit.heart),
                Card(Rank.three, Suit.diamond),
                Card(Rank.three, Suit.spade),
                Card(Rank.four, Suit.club),
                Card(Rank.four, Suit.heart),
                Card(Rank.four, Suit.diamond),
                Card(Rank.four, Suit.spade),
                Card(Rank.five, Suit.club),
                Card(Rank.five, Suit.heart),
                Card(Rank.five, Suit.diamond),
                Card(Rank.five, Suit.spade),
                Card(Rank.six, Suit.club),
                Card(Rank.six, Suit.heart),
                Card(Rank.six, Suit.diamond),
                Card(Rank.six, Suit.spade),
                Card(Rank.seven, Suit.club),
                Card(Rank.seven, Suit.heart),
                Card(Rank.seven, Suit.diamond),
                Card(Rank.seven, Suit.spade),
                Card(Rank.eight, Suit.club),
                Card(Rank.eight, Suit.heart),
                Card(Rank.eight, Suit.diamond),
                Card(Rank.eight, Suit.spade),
                Card(Rank.nine, Suit.club),
                Card(Rank.nine, Suit.heart),
                Card(Rank.nine, Suit.diamond),
                Card(Rank.nine, Suit.spade),
                Card(Rank.ten, Suit.club),
                Card(Rank.ten, Suit.heart),
                Card(Rank.ten, Suit.diamond),
                Card(Rank.ten, Suit.spade),
                Card(Rank.jack, Suit.club),
                Card(Rank.jack, Suit.heart),
                Card(Rank.jack, Suit.diamond),
                Card(Rank.jack, Suit.spade),
                Card(Rank.queen, Suit.club),
                Card(Rank.queen, Suit.heart),
                Card(Rank.queen, Suit.diamond),
                Card(Rank.queen, Suit.spade),
                Card(Rank.king, Suit.club),
                Card(Rank.king, Suit.heart),
                Card(Rank.king, Suit.diamond),
                Card(Rank.king, Suit.spade)
            ]
        )
