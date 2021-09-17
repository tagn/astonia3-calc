import pytest

from src.stats import *

@pytest.fixture
def stat():
    return Stat("Sword", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1)

def test_set_base(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    assert stat.cost == 21
    assert stat.value == 1
    assert stat.total_xp_used == 0

def test_increase(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    stat.increase(PlayerClass.WARRIOR)
    assert stat.cost == 34
    assert stat.value == 2

def test_decrease(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    stat.increase(PlayerClass.WARRIOR)
    stat.decrease(PlayerClass.WARRIOR)
    assert stat.cost == 21
    assert stat.value == 1

def test_multiple_increase_decrease(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    for _ in range(5):
        stat.increase(PlayerClass.WARRIOR)
    assert stat.cost == 133
    assert stat.value == 6
    for _ in range(5):
        stat.increase(PlayerClass.WARRIOR)
    assert stat.cost == 409
    assert stat.value == 11
    for _ in range(5):
        stat.decrease(PlayerClass.WARRIOR)
    assert stat.cost == 133
    assert stat.value == 6
    for _ in range(5):
        stat.decrease(PlayerClass.WARRIOR)
    assert stat.cost == 21
    assert stat.value == 1
