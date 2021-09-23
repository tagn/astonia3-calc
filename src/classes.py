import stat_pool

from stats import Stat


class BaseClass:
    """Base of all Classes"""

    skills: list[Stat]

    def __init__(self):
        self.skills = stat_pool.common


class WarriorClass(BaseClass):
    """Non-arched Warrior Class"""

    def __init__(self):
        super().__init__()
        self.skills += stat_pool.warrior


class ArchWarriorClass(WarriorClass):
    """Arched Warrior Class"""

    def __init__(self):
        super().__init__()
        self.skill += stat_pool.arch_warrior


class MageClass:
    """Non-arched Mage Class"""

    def __init__(self):
        super().__init__()
        self.skills += stat_pool.mage


class ArchMageClass(MageClass):
    """Arched Mage Class"""

    def __init__(self):
        super().__init__()
        self.skills += stat_pool.arch_mage


class SeyanClass:
    """Non-arched Seyan'du Class"""

    def __init__(self):
        super().__init__()
        self.skills += stat_pool.warrior
        self.skills += stat_pool.mage


class ArchSeyanClass:
    """Arched Seyan'du Class"""

    def __init__(self):
        super().__init__()
