from __future__ import annotations
from random import randint

class Spell:

    name: str
    description: str
    mana: int
    damage: int

    def __init__(self, name: str, description: str, mana: int, damage: int):
        self.__name = name
        self.__description = description
        self.__mana = mana
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_mana(self):
        return self.__mana

    def get_description(self):
        return self.__description

    def get_damage(self):
        return self.__damage

    def set_mana(self, mana: str):
        self.__mana = mana

    def set_damage(self, damage: str):
        self.__damage = damage


    def __str__(self):
        return (f"Название заклинания:{self.__name} \nРасход маны:{self.__mana}\n"
                f"Описание:{self.__description}")

class Hogwarts:

    students: HogwartsStudent
    spells: Spell

    def __init__(self, students=None, spells=None):
        self.__students = students or []
        self.__spells = spells or []

    def get_students(self):
        return self.students

    def get_spell(self):
        return self.spells

    def enroll_student(self, student: HogwartsStudent):
        self.__students.append(student)

    def teach_spell(self, spell: Spell):
        self.__spells.append(spell)

    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent):
        pass