'''
Import required module(s).
'''
from transport.car import Car
import transport.truck


'''
Instantiate Car and Truck objects (subclasses of the Vehicle superclass).
'''
car   = Car('ABC123', 'Holden', '2012')
truck = transport.truck.Truck('AAA111', 'Fuso', '2011')


'''
Print the output of a method in the Vehicle superclass.
'''
print(car.describeVehicle())


'''
Set vehicle colour then print the output of method in the Vehicle superclass.
'''
truck.set_colour('red');
print(truck.describeVehicle())


'''
Dump object structure.
'''
print(car.__dict__)
print(truck.__dict__)
