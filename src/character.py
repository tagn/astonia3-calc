from dataclasses import dataclass

from stats import PlayerClass, Stat

@dataclass
class Character:
    name: str
    level: float
    exp: float
    playerclass: PlayerClass
    stats: list[Stat]