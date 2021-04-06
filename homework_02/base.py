from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload


class Vehicle(ABC):
    """ defaults """
    weight = 1500
    started = False
    fuel = 100
    fuel_consumption = 2 # per 1 km


    def __init__(self, weight, fuel, fuel_consumption):

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):

        if self.started is True and self.fuel > 0:
            return self.started
        else:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise(LowFuelError)
                return False


    def move(self, distance):

        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
            return True
        else:
            raise(NotEnoughFuel)
            return False
