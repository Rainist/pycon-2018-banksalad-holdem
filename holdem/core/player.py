from dataclasses import dataclass
from typing import Callable


@dataclass
class Player:
    name: str
    bet: Callable[..., int]
