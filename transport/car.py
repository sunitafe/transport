from transport.vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, make, model):

        super().__init__(make, model)     
        self.type = 'car'
        self.rego_number = 'ABC123'
