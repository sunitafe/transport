import transport.fleet
import transport.car
import transport.truck

f = transport.fleet.Fleet('Horsham')
a = transport.car.Car('Holden', 'Monaro')
b = transport.truck.Truck('Mack', 'Semi')
c = transport.car.Car('Holden', 'Torana')
d = transport.truck.Truck('Kenworth', 'Monsta')

f.addVehicle(a)
f.addVehicle(b)
f.addVehicle(c)
f.addVehicle(d)

print(f.vehicles[1].type)

print(a.describeVehicle())

print(b.describeVehicle())

print(f.listVehicles())

print(f.depot.location)
