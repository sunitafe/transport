from transport.vehicle import Vehicle

# 'Car' is a subclass of 'Vehicle'
class Car(Vehicle):

    def __init__(self, rego, make, year):

        # Call superclass's __init__ method
        super().__init__(rego, make, year)     


        # Set some instance variables true of all fleet cars
        self.type = 'car'
        self.wheels = '4'
        self.fuel = 'petrol'
