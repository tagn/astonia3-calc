#!/usr/bin/env python3
import math

from enum import IntEnum, Enum, auto
from dataclasses import dataclass, field


class PlayerClass(Enum):
    WARRIOR = auto()
    MAGE = auto()
    SEYAN = auto()

class Attr(Enum):
    WIS = auto()
    INT = auto()
    AGI = auto()
    STR = auto()
    NONE = auto()

class Group(Enum):
    RES = auto()
    ATTR = auto()
    STATIC = auto()
    PRIMARY = auto()
    SECONDARY = auto()
    TERTIARY = auto()
    BONUS = auto()

class Cost(IntEnum):
    STATIC = 0
    SKILL = 1
    ATTR = 2
    RES = 3

@dataclass
class Stat:
    name: str
    bases: list[Attr]
    skill_type: Cost
    group: int
    minimum: int
    value: int = field(init=False)
    cost: int = 0

    def __post_init__(self):
        self.value = self.minimum

    def __increase_value(self):
        pass

    def __decrease_value(self):
        pass

    def __increase_cost(self):
        pass

    def __decrease_cost(self):
        pass

    def increase(self, current: int, char_class: PlayerClass):
        nr = current - self.minimum + 1 + 5
        multi = 4 if char_class == PlayerClass.SEYAN else 1
        return math.floor(nr * nr * nr * int(self.skill_type) * multi / 10)

    def decrease(self):
        pass

