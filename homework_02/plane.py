"""
создайте класс `Plane`, наследник `Vehicle`
"""

from dataclasses import dataclass, field
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

@dataclass
class Plane(Vehicle):
    """ defaults """
    cargo: int
    weight: int
    fuel: int
    fuel_consumption: int
    max_cargo = 10000


    def __init__(self, weight, fuel, fuel_consumption, max_cargo):

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
        self.cargo = 0


    def load_cargo(self, new_cargo):

        if self.cargo + new_cargo > self.max_cargo:
            raise(CargoOverload)
            return self.cargo
        else:
            self.cargo += new_cargo
            return self.cargo


    def remove_all_cargo(self):

        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
