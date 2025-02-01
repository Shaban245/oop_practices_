from __future__ import annotations

class Athlete:
    name: str
    age: int
    sport: str
    is_active: bool
    list_achievements: list

    def __init__(self, name, age, sport, is_active = True,list_achievements = None):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__is_active = is_active
        self.__list_achievements = []

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)

    def get_sport(self,):
        print(self.__sport)

    def get_status(self):
        print(self.__is_active)

    def get_achievements(self):
        print(self.__list_achievements)

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_sport(self, sport):
        self.__sport = sport

    def set_is_active(self):
        if self.__is_active == True:
            self.__is_active = False
        else:
            self.__is_active = True

    def add_achievements(self, Achievements):
        self.__list_achievements.append(Achievements)

    def remove_achievements(self, Achievements):
        self.__list_achievements.remove(Achievements)

    def __str__(self):
        print(f"имя {self.__name}\n"
              f"возраст {self.__age}\n"
              f"спорт {self.__sport}\n"
              f"занимается в данный момент {self.__is_active}\n"
              f"{self.__list_achievements}")


class Achievements:
    achievements: str
    sport: str

    def __init__(self, achievements, sport):
        self.__achievements = achievements
        self.__sport = sport

    def get_achievements(self):
        print(self.__achievements)

    def get_sport(self):
        print(self.__sport)

    def __str__(self):
        return (f"{self.__achievements}\n"
                f"{self.__sport}")
