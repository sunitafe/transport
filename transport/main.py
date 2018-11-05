from fleet import Fleet
from car import Car
from truck import Truck

f = Fleet()
a = Car('Holden', 'Monaro')
b = Truck('Mack', 'Semi')
c = Car('Holden', 'Torana')
d = Truck('Kenworth', 'Monsta')

z = f.addVehicle(a)

'''
f.addVehicle(a)
f.addVehicle(b)
f.addVehicle(c)
f.addVehicle(d)
'''
