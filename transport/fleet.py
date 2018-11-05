from transport.depot import Depot

class Fleet:

    def __init__(self, depot):

        self.vehicles = []
        self.depot = Depot(depot)

    def addVehicle(self, vehicle):

        self.vehicles.append(vehicle)


    def listVehicles(self):

        data = ''

        for v in self.vehicles:

            data += "{make} {model} {rego}\n".format(make = v.make, model = v.model, rego = v.rego_number)

        return data

                
