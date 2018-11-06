from transport.vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, rego, make, year):

        super().__init__(rego, make, year)     

        self.type = 'car'
        self.wheels = '4'
        self.fuel = 'petrol'
