import transport.fleet
import transport.car
import transport.truck

f = transport.fleet.Fleet()
a = transport.car.Car('Holden', 'Monaro')
b = transport.truck.Truck('Mack', 'Semi')
c = transport.car.Car('Holden', 'Torana')
d = transport.truck.Truck('Kenworth', 'Monsta')

z = f.addVehicle(a)

'''
f.addVehicle(a)
f.addVehicle(b)
f.addVehicle(c)
f.addVehicle(d)
'''
