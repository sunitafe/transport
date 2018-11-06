from transport.depot import Depot

class Fleet:

    def __init__(self, depot):

        self.vehicles = []
        self.depot = Depot(depot)


    def addVehicle(self, vehicle):

        self.vehicles.append(vehicle)


    def listVehicles(self):

        data = "\nVehicles in the {depot} fleet:\n".format(depot = self.depot.location)
        count = 1

        for v in self.vehicles:

            data += str(count) + ": {year} {make} {rego}\n".format(year = v.year, make = v.make, rego = v.rego)
            count += 1

        data += "\n"

        return data

                
