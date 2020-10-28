car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("1 + 1 = 3 ? " + str((1 + 1) == 3))

str1 = "love"
str2 = "peace"
print("str1 == str2 ? " + str1 == str2)
print("str1 == str2 ?" + str1 != str2)
print("LOVE".lower() == str1)
num1 = 1
num2 = 2
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print(num1 >= 1 and num2 == 2)
print(num1 > 0 or num2 < 3)
list = ['a','b','c']
print('a' in list)
print('d' not in list)

alien_color = 'green'
if alien_color == 'green':
	print("Player get 5 points.")
if alien_color != 'green':
	print("null")

if alien_color == 'green':
	print("Player get 5 points.")
else:
	print("Player get 10 points.")

if alien_color == 'green':
	print("Player get 5 points.")
elif alien_color == 'yellow':
	print("Player get 10 points.")
elif alien_color == 'red':
	print("Player get 15 points.")

age = 27
if age < 2:
	print("婴儿")
elif age >= 2 and age <= 4:
	print("蹒跚学步")
elif age >= 4 and age <= 13:
	print("儿童")
elif age >= 13 and age <= 20:
	print("青少年")
elif age >= 20 and age <=65:
	print("成年人")
else:
	print("老年人")

favorite_fruits = ['apple', 'orange', 'banana']
if 'apple' in favorite_fruits:
	print("You really like apple!")
elif 'orange' in favorite_fruits:
	print("You really like orange!")
elif 'banana' in favorite_fruits:
	print("You really like banana!")

user_list = ['blues', 'admin', 'sky', 'cloud', 'star']

for user in user_list:
	if user == 'admin':
		print("Hello " + user + ", would you like to see a status report?")
	else:
		print("Hello " + user + ", thank you for logging in again")

for user in user_list:
	user_list.pop()

if user_list:
	print("We need to find some users!")

current_users = ['blues', 'admin', 'sky', 'cloud', 'star']
new_users = ['zhangsan', 'lisi', 'BLUES', 'blues', 'sky']

for n_user in new_users:
	if (n_user in current_users) or (n_user.lower() in current_users):
		print(n_user + ", This name used!")
	else:
		print(n_user + ", This name not used!")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	value = str(number)
	if number == 1:
		print(value + "st")
	elif number == 2:
		print(value + "nd")
	elif number == 3:
		print(value + "rd")
	else:
		print(value + "th")
		