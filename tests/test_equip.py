import pytest

from src.equip import *


def test_item_creation():
    item = Item(EquipSlot.RING1, ItemType.SOFT)
    assert item.slot == EquipSlot.RING1


@pytest.fixture
def item():
    return Item(EquipSlot.RING1, ItemType.SOFT)

@pytest.fixture
def loadout():
    return Loadout()

def test_add_stat(item):
    item.add_stat("Strength", 8)
    assert item.stats["Strength"] == 8


def test_remove_stat(item):
    item.add_stat("Strength", 8)
    item.remove_stat("Strength")
    assert "Strength" not in item.stats.keys()


def test_changing_stat_value(item):
    item.add_stat("Strength", 8)
    item.add_stat("Strength", 10)
    assert item.stats["Strength"] == 10


def test_too_many_item_stats(item):
    item.add_stat("Strength", 8)
    item.add_stat("Agility", 9)
    item.add_stat("Intuition", 7)
    item.add_stat("Wisdom", 13)
    assert sorted(item.stats.keys()) == sorted(["Strength", "Agility", "Intuition"])


def test_add_item_to_loadout(loadout):
    item = Item(EquipSlot.RING1, ItemType.SOFT, {"Strength": 8})
    loadout.add_item(item)
    assert len(loadout.items) == 1


def test_add_duplicate_item_to_loadout(loadout):
    item = Item(EquipSlot.RING1, ItemType.SOFT, {"Strength": 8})
    loadout.add_item(item)
    loadout.add_item(item)
    assert len(loadout.items) == 1


def test_remove_item_from_loadout(loadout):
    item1 = Item(EquipSlot.RING1, ItemType.SOFT, {"Strength": 8})
    item2 = Item(EquipSlot.RING2, ItemType.SOFT, {"Agility": 12})
    loadout.add_item(item1)
    loadout.add_item(item2)
    assert len(loadout.items) == 2
    loadout.remove_item(item2)
    assert len(loadout.items) == 1
