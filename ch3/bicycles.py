bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'ducati')
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

motorcycles.append('honda')
motorcycles.remove('honda')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
cars.sort(reverse=True)
print("暂时性排序:")
print(sorted(cars))
print("原来的排序:")
print(cars)
print("暂时性倒序:")
print(sorted(cars,reverse=True))

cars.reverse()
print(cars)

print(len(cars))