import json
import logging
import os

from .core.cards import Card
from .core.game import Game


LOG_FILE_NAME = 'play.log'


logging.basicConfig(
    filename=LOG_FILE_NAME,
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
        ],
        'all_in': g.all_in
    }))


def error(msg: str):
    logging.error(msg)


def on_finish():
    fpath = os.path.join(os.getcwd(), LOG_FILE_NAME)
    with open(fpath, 'r') as f:
        lines = f.readlines()

    with open(fpath, 'w') as f:
        for idx, l in enumerate(lines):
            if idx > 0 and lines[idx - 1] == l:
                continue
            f.write(l)
