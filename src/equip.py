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


class ItemType(Enum):
    SOFT = auto()
    ARMOR = auto()
    WEAPON = auto()


class WeaponType(Enum):
    SWORD = auto()
    TWOHAND = auto()
    DAGGER = auto()
    STAFF = auto()
    GLOVE = auto()


class ItemQuality(Enum):
    UE = auto()
    SE = auto()
    GE = auto()


@dataclass
class Item:
    slot: EquipSlot
    type: ItemType
    stats: dict = field(default_factory=dict)
    quality: ItemQuality = field(default=ItemQuality.UE)

    def add_stat(self, stat: str, mod: int = 1):
        if len(self.stats.keys()) < 3 or stat in self.stats.keys():
            self.stats[stat] = mod
        else:
            print(f"Not enough space to add stat: {stat}={mod}")

    def remove_stat(self, stat: str):
        del self.stats[stat]


@dataclass
class Loadout:
    items: list[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        if item.slot not in [s.slot for s in self.items]:
            self.items.append(item)
        else:
            print(f"Unable to add {item} to Loadout")

    def remove_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
