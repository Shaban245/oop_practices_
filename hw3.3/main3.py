class Robot:
    number:int
    model: str
    task: str
    battery_charge: int
    is_work: bool

    def __init__(self,number, model, task, battery_charge, is_work = None):
        self.__number = number
        self.__model = model
        self.__task = task
        self.__battery_charge = battery_charge
        self.__is_work = is_work

    def get_number(self):
        return self.__number

    def get_model(self):
        return self.__model

    def get_task(self):
        return self.__task

    def get_battery_charge(self):
        return self.__battery_charge

    def get_is_work(self):
        return self.__is_work

    def change_charge(self, charge):
        self.__battery_charge = charge

    def start_work(self):
        self.__is_work = True

    def end_work(self):
        self.__is_work = False

    def set_task(self, new_task):
        self.__task = new_task

    def set_model(self, new_model):
        self.__model = new_model

    def __str__(self):
        print(f"состояние  заряда батареи : {self.__battery_charge}")