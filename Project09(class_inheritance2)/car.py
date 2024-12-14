from electric import Electric
from petrol import Petrol

class Car(Petrol, Electric):
    steering_wheel_type = None
    airbag = None