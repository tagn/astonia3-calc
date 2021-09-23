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
    mod: int = field(init=False)
    value: int = field(init=False)
    cost: int = field(init=False)
    total_xp_used: int = field(init=False)

    def __post_init__(self):
        self.total_xp_used = 0
        self.value = self.minimum

    def set_base_cost(self, char_class):
        self.cost = self.__change_cost(0, char_class)
        self.total_xp_used = 0

    def __change_value(self, modifier):
        self.value += modifier

    def __change_cost(self, modifier: int, char_class: PlayerClass):
        nr = self.value + modifier - self.minimum + 1 + 5
        if char_class == PlayerClass.SEYAN:
            return math.floor(nr * nr * nr * int(self.skill_type) * 4 / 30)
        else:
            return math.floor(nr * nr * nr * int(self.skill_type) / 10)

    def increase(self, char_class: PlayerClass):
        self.total_xp_used += self.cost
        self.__change_value(1)
        self.cost = self.__change_cost(0, char_class)

    def decrease(self, char_class: PlayerClass):
        self.cost = self.__change_cost(-1, char_class)
        self.total_xp_used -= self.cost
        self.__change_value(-1)
