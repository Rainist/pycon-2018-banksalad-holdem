from dataclasses import dataclass
from typing import List

from .core.cards import Card


@dataclass
class Me:
    chips: int
    cards: List[Card]


@dataclass
class Other:
    chips: int
    bet_amt: int
    died: bool
