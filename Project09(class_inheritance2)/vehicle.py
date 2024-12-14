class Vehicle:
    cylinders = None
    horse_power = None
    abs_brakes = None
    man_year = None
    plate = None

    def __repr__(self):
        return str(self.__dict__)