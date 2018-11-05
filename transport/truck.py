from .vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, make, model):

        super().__init__(make, model)     
        self.type = 'truck'
