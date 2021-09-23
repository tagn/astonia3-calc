import pytest

from src.stats import *


@pytest.fixture
def stat():
    return Stat("Sword", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1)


def verify_stat_values(stat_instance, cost, value):
    assert stat_instance.cost == cost
    assert stat_instance.value == value


def test_set_base(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    verify_stat_values(stat, 21, 1)


def test_increase(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    stat.increase(PlayerClass.WARRIOR)
    verify_stat_values(stat, 34, 2)


def test_decrease(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    stat.increase(PlayerClass.WARRIOR)
    stat.decrease(PlayerClass.WARRIOR)
    verify_stat_values(stat, 21, 1)


def test_multiple_increase_decrease(stat):
    stat.set_base_cost(PlayerClass.WARRIOR)
    for _ in range(5):
        stat.increase(PlayerClass.WARRIOR)
    verify_stat_values(stat, 133, 6)
    for _ in range(5):
        stat.increase(PlayerClass.WARRIOR)
    verify_stat_values(stat, 409, 11)
    for _ in range(5):
        stat.decrease(PlayerClass.WARRIOR)
    verify_stat_values(stat, 133, 6)
    for _ in range(5):
        stat.decrease(PlayerClass.WARRIOR)
    verify_stat_values(stat, 21, 1)
