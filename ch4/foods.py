my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three items in the list are:")
for item in my_foods[:3]:
	print(item)

print("\nThree items from the middle of the list are:")
for item in my_foods[1:3]:
	print(item)

print("\nThe last three items in the list are:")
for item in my_foods[-3:]:
	print(item)