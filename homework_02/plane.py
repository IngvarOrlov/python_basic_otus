from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = None

    def __init__(self, max_cargo):
        super().__init__()
        self.max_cargo = max_cargo

    def load_cargo(self, val):
        if self.cargo + val > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += val

    def remove_all_cargo(self):
        val = self.cargo
        self.cargo = 0
        return val
