from __future__ import annotations
class Wizard:
    name: str
    house: str
    magic_lvl: int
    status: str
    spells: list

    def __init__(self, name , house, magic_lvl, status, spells = None):
        self.__name = name
        self.__house = house
        self.__magic_lvl = magic_lvl
        self.__status = status
        self.__spells = []

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_magic_lvl(self):
        return self.__magic_lvl

    def get_status(self):
        return self.__status

    def get_spells(self):
        return self.__spells

    def add_spell(self, Spell):
        self.__spells.append(Spell)

    def remove_spell(self, Spell):
        self.__spells.remove(Spell)

    def set_house(self, new_house):
        self.__house = new_house

    def set_status(self, new_status):
        self.__status = new_status

    def set_magic_lvl(self, new_magic_lvl):
        self.__magic_lvl = new_magic_lvl

class Spell:
    name: str
    type: str
    difficulty_level: int
    description: str

    def __init__(self, name, type, difficulty_level, description):
        self.__name = name
        self.__type = type
        self.__difficulty_level = difficulty_level
        self.__description = description

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_difficulty_level(self):
        return self.__difficulty_level

    def get_description(self):
        return self.__description

    def set_name_(self,name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_difficulty_level(self, difficulty_level):
        self.__difficulty_level = difficulty_level

    def set_description(self, description ):
        self.__description = description

    def __str__(self):
        return (f"имя {self.__name}\n"
                f"тип {self.__type}\n"
                f"уровень сложности {self.__difficulty_level}\n"
                f"описание {self.__description}\n")