from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("You should refuel!")

    def move(self, distance):
        if distance * self.fuel_consumption <= self.fuel:
            self.fuel -= distance * self.fuel_consumption
            print("It is enough fuel! Let's go!")
            # return True
        else:
            # raise NotEnoughFuel("Not enough fuel for this distance!")
            raise NotEnoughFuel




