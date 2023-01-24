from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is True:
            return
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance >= distance:
            self.fuel = self.fuel - (distance * self.fuel_consumption)
            return self.fuel
        raise exceptions.NotEnoughFuel

