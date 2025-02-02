from __future__ import annotations

class Student:
    first_name: str
    second_name: str
    age: int
    average_score: float

    def __init__(self, first_name, second_name, age, average_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_score = average_score

    def get_first_name(self):
        return self.first_name

    def get_second_name(self):
        return self.second_name

    def get_age(self):
        return self.age

    def get_average_score(self):
        return self.average_score

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_second_name(self, new_second_name):
        self.second_name = new_second_name

    def set_age(self, new_age):
        self.age = new_age

    def set_average_score(self, new_average_score):
        self.average_score = new_average_score

    def is_bigger(self, s2: Student):
        if self.average_score > s2.average_score:
            return True

    def is_smaller(self, s2: Student):
        if self.average_score < s2.average_score:
            return True

    def is_equal(self, s2: Student):
        if self.average_score == s2.average_score:
            return True

    def is_not_equal(self, s2: Student):
        if self.average_score != s2.average_score:
            return True


