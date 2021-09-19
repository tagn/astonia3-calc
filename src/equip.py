from enum import Enum, auto
from dataclasses import dataclass, field

class EquipSlot(Enum):
    RING1 = auto()
    WEAPON = auto()
    RING2 = auto()
    AMMY = auto()
    HEAD = auto()
    CAPE = auto()
    CHEST = auto()
    BELT = auto()
    WRIST = auto()
    LEG = auto()
    BOOT = auto()

class WeaponType(Enum):
    SWORD = auto()
    TWOHAND = auto()
    DAGGER = auto()
    STAFF = auto()
    GLOVE = auto()

@dataclass
class ItemStat:
    name: str
    value: int

@dataclass
class Item:
    slot: EquipSlot
    modifiers: list[ItemStat]
    base_stat: str = field(init=False)
    value: int = field(init=False)

    def __post_init__(self, requires: int = 0):
        if self.slot == EquipSlot.WEAPON:

@dataclass
class Equipment:
    slot: EquipSlot
    type: str
    skill: int
    base_stat: float
    stat1: int
    stat2: int
    stat3: int

    def __post_init__(self):
        self.base_stat

@dataclass
class Loadout:
