requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
		print("Hold the anchovies!")

age = 18
print(age == 18)

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
	print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")

if 'mushrooms' in requested_topping:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_topping:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_topping:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
else:
	print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers',
					 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")