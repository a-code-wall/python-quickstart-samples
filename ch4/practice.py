pizzas = ['芝士披萨', '培根披萨', '鲜虾披萨']
for pizza in pizzas:
	print(pizza + ", 真好吃!")
	print("I like pepperoni pizza")
print("I really love pizza!")

cats = ['家猫', '熊猫', '狸猫']
for cat in cats:
	print(cat)
	print("A dog would make a great pet")
print("Any of these animals would make a great pet!")	

for number in range(1,21):
	print(number)

list = [value for value in range(1,1000001)]
# for l in list:
	# print(l)

print(min(list))
print(max(list))
print(sum(list))

odd_numbers = [value for value in range(1,20,2)]
for odd in odd_numbers:
	print(odd)

mul_list = [value for value in range(3,31,3)]
for n in mul_list:
	print(n)

cube_list = [value ** 3 for value in range(1,11)]
for c in cube_list:
	print(c)

my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = my_foods[:]
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

my_foods.append("芝士披萨")
friend_foods.append("培根披萨")
print("My favorite pizzas are:")
for food in my_foods:
	print(food)
print("My friend's favorite pizzas are:")
for food in friend_foods:
	print(food)	

simple_foods = ('炒饭','炒粉','炒油面','炒河粉','炒泡面')
for food in simple_foods:
	print(food)
simple_foods = ('炒饭','炒粉','炒油面','扁食','拌面')
for food in simple_foods:
	print(food)