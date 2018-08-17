import json
import logging

from .core.cards import Card
from .core.game import Game


logging.basicConfig(
    filename='play.log',
    filemode='w',
    level=logging.INFO
)


def _log_card(c: Card) -> dict:
    return {
        'suit': c.suit.value,
        'rank': c.rank.value
    }


def log(g: Game):
    logging.info(json.dumps({
        'round': g.round,
        'acc_chips': g.acc_chips,
        'community_cards': [_log_card(c) for c in g.deck.community_cards],
        'players': [
            {
                'name': p.player.meta.name,
                'cards': [_log_card(c) for c in p.status.cards],
                'bet_amt': p.status.bet_amt,
                'chips': p.player.chips,
                'died': p.status.died
            } for p in g.players
        ]
    }))


def error(msg: str):
    logging.error(msg)
