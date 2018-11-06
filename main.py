'''
Import required modules.
These are all located in the transport/ directory.
'''
import transport.fleet
import transport.car
import transport.truck


'''
Instantiate a Fleet object.
This object will contain a Depot attribute with location in Horsham.
''' 
f = transport.fleet.Fleet('Horsham')


'''
Instantiate a number of Car and Truck objects.
Car and Truck objects are subclasses of the Vehicle superclass.
'''
a = transport.car.Car('ABC123', 'Holden', '2012')
b = transport.truck.Truck('XYZ123', 'Misubishi', '2009')
c = transport.car.Car('AAA456', 'Ford', '2017')
d = transport.truck.Truck('ABC789', 'Isuzu', '2014')


'''
Add the vehicles instantiated above to the Fleet object.
'''
f.addVehicle(a)
f.addVehicle(b)
f.addVehicle(c)
f.addVehicle(d)


'''
List all the vehicles in the fleet.
This calls a method in the Fleet class.
'''
print(f.listVehicles())


'''
Print the output of a method in the Vehicle superclass.
'''
print(a.describeVehicle())
print(b.describeVehicle())


'''
Dump object structure.
'''
print(f.__dict__)
print(a.__dict__)
print(a.__class__)
