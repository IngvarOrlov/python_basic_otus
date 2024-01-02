from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1600, fuel=100, fuel_consumption=10):
        super().__init__()
        self._weight = weight
        self.started = False
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, int) and 500 <= new_weight <= 2000:
            self._weight = new_weight
        else:
            print("New weight is not correct")

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, new_val):
        if isinstance(new_val, int) and 0 <= new_val <= 200:
            self._fuel = new_val
        else:
            print("New fuel value incorrect")

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if isinstance(value, int) and 1 <= value <= 50:
            self._fuel_consumption = value
        else:
            print("New fuel consumption value incorrect")

    def start(self):
        if not self.started:
            if self._fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Not enough fuel to start your car!")

    def move(self, distance: int | float):
#        rest_of_fuel = self._fuel - distance*self._fuel_consumption
#        if rest_of_fuel < 0:
#            raise NotEnoughFuel("Not enough fuel to travel this far")
#        else:
#            self._fuel = rest_of_fuel
        if distance * self.fuel_consumption > self.fuel:
            raise NotEnoughFuel
        self.fuel -= distance * self.fuel_consumption
