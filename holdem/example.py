from typing import List

from .core.cards import Card
from .player import Me, Other


def always_bet(
    me: Me,
    bet_players: List[Other],
    betting_players: List[Other],
    community_cards: List[Card],
    min_bet_amt: int,
    max_bet_amt: int,
    total_bet_amt: int
) -> int:
    if me.chips >= min_bet_amt:
        return min(max_bet_amt, min_bet_amt)
    else:
        return 0
