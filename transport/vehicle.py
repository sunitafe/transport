class Vehicle:

    registered_owner = 'Fleet Management Pty Ltd'

    def __init__(self, rego, make, year):

        self.rego = rego
        self.make = make
        self.year = year


    def describeVehicle(self):

        return "Vehicle: {year} {make}\nRegistration Number: {rego}\nOwner: {owner}\nType: {type}\nNumber of Wheels: {wheels}\nFuel: {fuel}\n\n".format(
            year = self.year, 
            make = self.make, 
            rego = self.rego,
            owner = Vehicle.registered_owner,
            type = self.type,
            wheels = self.wheels,
            fuel = self.fuel)


