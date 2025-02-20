from abc import ABC, abstractmethod
from __future__ import annotations

class AAccount(ABC):

    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def check_balance(self):
        print(f"ваш счет составляет - {self.balance}")

class DebitAccount(AAccount):

    def __init__(self, balance):
        super().__init__(balance)

    def up_balance(self, value: float):

        self.balance += value

    def down_balance(self, value):
        self.balance -= value

    def check_balance(self):
        print(f"ваш счет составляет - {self.balance}")


class CreditCard(AAccount):
    def __init__(self, duty, balance):
        super().__init__(duty)
        self.balance = balance
        self.duty = duty

    def check_balance(self):
        print(f"ваш счет составляет - {self.balance}")

    def take_a_loun(self, value):
        self.balance += value
        self.duty += value

    def pey_duty(self, value):
        if value < self.balance:
            self.balance -= value
            self.duty -= value

    def up_balance(self, value: float):

        self.balance += value

    def down_balance(self, value):
        self.balance -= value


class ABankEmployee(ABC):

    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    @abstractmethod
    def start_working(self):
        pass


class Manager(ABankEmployee):

    def __init__(self, employees: Cashier, name, title, salary):
        super().__init__(name, title, salary)
        self.employees = []

    def fire_an_employee(self, employee):
        self.employees.append(employee)

    def hire_an_employee(self, employee):
        self.employees.remove(employee)

    def start_working(self):
        pass

class Cashier(ABankEmployee):
    def __init__(self, name , title, salary):
        super().__init__(name, title, salary)

    def start_working(self):
        pass

