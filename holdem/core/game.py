from dataclasses import dataclass
from enum import IntEnum
from typing import List

from .cards import Card
from .deck import Deck
from .player import Player as MetaPlayer


@dataclass
class PlayerGameStatus:
    cards: List[Card]
    bet_amt: int
    died: bool


@dataclass
class Player:
    meta: MetaPlayer
    chips: int


@dataclass
class ActivePlayer:
    player: Player
    status: PlayerGameStatus

    def __repr__(self):
        return self.player.meta.name


@dataclass
class Game:
    round: int
    deck: Deck
    players: List[ActivePlayer]
    acc_chips: int
    is_all_in: bool


class GameState(IntEnum):
    bet = 1
    flop = 2
