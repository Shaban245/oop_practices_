class Employee:
    name: str
    title: str
    department: str
    salary: float
    experience: int
    completed_projects: list

    def __init__(self, name, title, departament, salary, expirience, completed_projects = None):
        self.__name = name
        self.__title = title
        self.__department = departament
        self.__salary = salary
        self.__experience = expirience
        self.__completed_projects = [52, 32,242 ,243243, 3]

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__title

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def get_experience (self):
        return self.__experience

    def get_projects(self):
        return self.__completed_projects


    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary

    def change_project(self, new_project: str):
            if new_project not in self.__completed_projects:
                self.__completed_projects.append(new_project)

    def remove_project(self, project: str):
        if project in self.__completed_projects:
            self.__completed_projects.remove(project)

    def set_title(self, title: str):
        if title != self.__title:
            self.__title = title

    def set_departament(self, departament):
        if self.__department != departament:
            self.__department = departament

    def __str__(self):
        print(f"имя сотрудника : {self.__name} \nдолжность : {self.__title} \nзарплата : {self.__salary} \nопыт работы : {self.__experience}")
        print("Выполненые проекты")
        for i in self.__completed_projects:
            print(i)

bebra = Employee("bebra", "пахан", "отдел продаж", 50000, 3)

bebra.__str__()