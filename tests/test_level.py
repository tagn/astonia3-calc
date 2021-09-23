import pytest

from src.level import *


def verify_xp_counts(lvl: PlayerLevel, total_exp: int, exp_to_next: int):
    assert lvl.total_exp == total_exp
    assert lvl.exp_to_next == exp_to_next


def test_level_1():
    verify_xp_counts(PlayerLevel(1), 1, 15)


def test_level_20():
    verify_xp_counts(PlayerLevel(20), 160000, 34481)


def test_level_55():
    verify_xp_counts(PlayerLevel(55), 9150625, 683871)


def test_level_69():
    verify_xp_counts(PlayerLevel(69), 22667121, 1342879)
