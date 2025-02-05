from __future__ import annotations

class Libary:
    name: str
    address: str
    books: list
    employees: list

    def __init__(self, name, address, books = None, employees = None):
        self.__name = name
        self.__address = address
        if books != None:
            self.__books = [books]
        else:
            self.__books= []
        if employees != None:
            self.__employees = [employees]
        else:
            self.__employees = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        return self.__books

    def get_employees(self):
        return self.__employees

    def set_address(self, address: str):
        return self.__address

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, book: Book):
        self.__books.remove(book)

    def add_employees(self, employees: Employees):
        self.__employees.append(employees)

    def remove_employess(self, employees:Employees):
        self.__employees.remove(employees)

    def __str__(self):
        return f"Название библиотеки: {self.__name} \nСписок книг: {self.__books} \nСписок работников: {self.__employees} адресс: {self.__address}"

class Book:
    name: str
    id: int
    year: int
    genre : list

    def __init__(self, name, id, year, genre=None):
        self.__name = name
        self.__id = id
        self.__year = year
        self.__genre = []
        if genre is not None:
            self.__genre.append(genre)

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_year(self):
        return self.__year
    def get_genre(self):
        return self.__genre

    def set_year(self, year):
        self.__year = year

    def add_genre(self, genre: Genre):
        self.__genre.append(genre.get_name())

    def remove_genre(self, genre):
        self.__genre.remove(genre.get_name())

    def __str__(self):
        return f"Название книги: {self.__name} \nID: {self.__id} \nГод: {self.__year} \nЖанры: {self.__genre}"

class ContactInfo:
    type: str
    value: str

    def __init__(self, type, value):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

class Employee:
    name: str
    position: str
    id: int
    contact_info: list
    def __init__(self, name, position, id, contact_info):
        self.__name = name
        self.__position = position
        self.__id = id
        self.__contact_info = None
        if contact_info != None:
            self.__contact_info = [contact_info]

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info

    def set_position(self, position):
        self.__position = position

    def add_contact_info(self,contact_info):
        self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info): 
        self.__contact_info.remove(contact_info)

    def __str__(self):
        return f"Имя: {self.__name} \nДолжность: {self.__position} \nID: {self.__id} \nКонтакты: {self.__contact_info}"


