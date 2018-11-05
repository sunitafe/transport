class Vehicle:

    rego_number = 'XYZ321'

    def __init__(self, make, model):

        self.make = make
        self.model = model
  
        self.number_of_wheels = 0
        self.colour = ''

    def describeVehicle(self):

        return "{make} {model} {rego_number}".format(make = self.make, model = self.model, rego_number = self.rego_number)
