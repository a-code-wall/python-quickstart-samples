cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'bmw'
print(car == 'bmw') #True

car = 'audi'
print(car == 'bmw') #False

car = 'Audi'
print(car == 'audi') #False

print(car.lower() == 'audi') #True
pritn(car)