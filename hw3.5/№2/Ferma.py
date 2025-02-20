from __future__ import annotations
from abc import ABC,abstractmethod

class AFarmAnimal(ABC):

    name: str
    weight: float

    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    @abstractmethod
    def move(self):
        pass


class Cow(AFarmAnimal):

    def __init__(self,calfs,  name, weight):
        super.__init__(name, weight)
        self.calfs = calfs

    def move(self):
        pass

    def eat_draw(self):
        print("корова кушает травку")


class Chicken(AFarmAnimal):

    def __init__(self, eggs: int, name, weight):
        super().__init__(eggs, name, weight)
        self.eggs = eggs

    def move(self):
        pass


class Sheep(AFarmAnimal):

    def __init__(self, wool: int, name, weight):
        super().__init__(wool, name, weight)
        self.wool = wool

    def move(self):
        pass


class AFarmEquipment(ABC):

    def __init__(self, speed: int):
        self.speed = speed

    @abstractmethod
    def move(self,):
        print(f"вы едете  со скорость {self.speed}")


class Tractor(AFarmEquipment):
    
    def __init__(self, speed):
        super().__init__(speed)
    
    def move(self,):
        pass
    
    def drive(self):
        print("дал газу")


class Harvester(AFarmEquipment):
    
    def __init__(self, harested_grain: int, speed ):
        super().__init__(speed)
        self.harested_grain = harested_grain


    def move(self,):
        pass

    def collect_grain(self, value):
        self.harested_grain += value


class Abuilding(ABC):

    def __init__(self, is_built: bool):
        self.is_built = False

    @abstractmethod
    def built(self):
        self.is_built = True


class AField(Abuilding):

    def __init__(self, planet_plants: list, is_built):
        super().__init__(is_built)
        self.planet_plants = []

    def built(self):
        self.is_built = True

    def planet(self, vegetable: Vegetable or GrainGroup):
        self.planet_plants.append(vegetable)


class GreenHouse(Abuilding):

    def __init__(self, is_built, temperature: float):
        super().__init__(is_built)
        self.temperature = temperature

    def built(self):
        self.is_built = True


class Vegetable:
    def __init__(self, name : str):
        self.name = name

class GrainGroup:
    def __init__(self, name : str):
        self.name = name