#!/usr/bin/env python3
from skill import Attr, Cost, Stat, PlayerClass, Group
from character import Character
import classes

def main():
    test = Stat("Sword", [Attr.INT, Attr.AGI, Attr.STR], Cost.SKILL, Group.PRIMARY, 1)
    print(test.increase(5, "warrior"))

    char = Character("Tag", 1.0, 0.0, PlayerClass.WARRIOR, classes.WarriorClass().skills)

if __name__ == "__main__":
    main()