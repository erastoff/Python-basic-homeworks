"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, add_cargo):
        if (self.cargo + add_cargo) <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        unload = self.cargo
        self.cargo = 0
        return unload





