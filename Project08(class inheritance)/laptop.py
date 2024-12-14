from electrical import Electrical


class Laptop(Electrical):
    def __init__(self, ram=None, cpu=None):
        self.ram = ram
        self.cpu = cpu
