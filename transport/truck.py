from transport.vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, rego, make, year):

        super().__init__(rego, make, year)     

        self.type = 'truck'
        self.wheels = '6'
        self.fuel = 'diesel'
