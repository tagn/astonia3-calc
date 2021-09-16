from skill import Attr, Cost, Stat, Group

common = [
    Stat("Hitpoints", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.RES, Group.RES, 10),
    Stat("Endurance", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.RES, Group.RES, 10),
    Stat("Mana", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.RES, Group.RES, 10),
    Stat("Wisdom", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.ATTR, Group.ATTR, 10),
    Stat("Intuition", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.ATTR, Group.ATTR, 10),
    Stat("Agility", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.ATTR, Group.ATTR, 10),
    Stat("Strength", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.ATTR, Group.ATTR, 10),
    Stat("Armor", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.STATIC, Group.STATIC, 0),
    Stat("Weapon", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.STATIC, Group.STATIC, 0),
    Stat("Light", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.STATIC, Group.STATIC, 0),
    Stat("Speed", [Attr.AGI, Attr.AGI, Attr.STR], Cost.STATIC, Group.STATIC, 0),
    Stat("Dagger", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1),
    Stat("Hand to Hand", [Attr.AGI, Attr.STR, Attr.STR], Cost.SKILL, Group.PRIMARY, 1),
    Stat("Staff", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1),
    Stat("Sword", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1),
    Stat("Two-Handed", [Attr.AGI, Attr.STR, Attr.STR], Cost.SKILL, Group.PRIMARY, 1),
    Stat("Bartering", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.TERTIARY, 1),
    Stat("Perception", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.TERTIARY, 1),
    Stat("Stealth", [Attr.INT, Attr.AGI, Attr.AGI], Cost.SKILL, Group.TERTIARY, 1),
    Stat("Immunity", [Attr.INT, Attr.WIS, Attr.STR], Cost.SKILL, Group.TERTIARY, 1),
    Stat("Profession", [Attr.NONE, Attr.NONE, Attr.NONE], Cost.SKILL, Group.BONUS, 1),
]
warrior = [
    Stat("Armor Skill", [Attr.AGI, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Attack", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Parry", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Warcry", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Tactics", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Surround Hit", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Body Control", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Speed Skill", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Regeneration", [Attr.STR, Attr.STR, Attr.STR], Cost.SKILL, Group.TERTIARY, 1),
]
arch_warrior = [
    Stat("Rage", [Attr.INT, Attr.STR, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
]
mage = [
    Stat("Bless", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Heal", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Freeze", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Magic Shield", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Lightning", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Fire", [Attr.INT, Attr.INT, Attr.WIS], Cost.SKILL, Group.SECONDARY, 1),
    Stat("Meditate", [Attr.WIS, Attr.WIS, Attr.WIS], Cost.SKILL, Group.TERTIARY, 1),
]
arch_mage = [
    Stat("Duration", [Attr.INT, Attr.WIS, Attr.STR], Cost.SKILL, Group.SECONDARY, 1),
]
