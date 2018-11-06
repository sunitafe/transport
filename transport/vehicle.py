class Vehicle:

    registered_owner = 'Fleet Management Pty Ltd'


    def __init__(self, rego, make, year):

        self.rego = rego
        self.make = make
        self.year = year

        self.colour = "white"


    def describeVehicle(self):

        data = ("\nVehicle: {year} {make}\n"
               "Registration Number: {rego}\n"
               "Owner: {owner}\n"
               "Type: {type}\n"
               "Number of Wheels: {wheels}\n"
               "Fuel: {fuel}\n"
               "Colour: {colour}\n").format(
            year = self.year, 
            make = self.make, 
            rego = self.rego,
            owner = Vehicle.registered_owner,
            type = self.type,
            wheels = self.wheels,
            fuel = self.fuel,
            colour = self.colour)

        return data


    def set_colour(self, colour):

        self.colour = colour


    def get_colour(self):

        return self.colour
