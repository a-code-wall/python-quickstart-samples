# 餐馆
class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("Restaurant's name is " + self.restaurant_name + 
			  " and cuisineType is " + self.cuisine_type)

	def open_restaurant(self):
		print("Restaurant is opening now!")

	def set_number_served(self,number):
		self.number_served = number

	def increment_number_served(self,number):
		self.number_served += number

restaurant = Restaurant('和平饭店', '中式')
print("饭店名: " + restaurant.restaurant_name + ", 类型: " + 
	  restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# # 三家餐馆
restaurant_1 = Restaurant('麦当劳', '西式')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# 用户
class User():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0
	def describe_user(self):
		print("user name is " + self.first_name.title() + " " + self.last_name +
			  " age is " + str(self.age))
	def greet_user(self):
		full_name = self.first_name.title() + " " + self.last_name
		print("Hello, " + full_name)
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0

user = User('bruce', 'lee', 33)
user.describe_user()
user.greet_user()

# 就餐人数
my_restaurant = Restaurant('我的饭店','好吃的')
print("有" + str(my_restaurant.number_served) + "在这家餐厅就餐过")
my_restaurant.number_served = 10
print("就餐人数现在到达了" + str(my_restaurant.number_served) + "人")
my_restaurant.set_number_served(20)
print("就餐人数现在为" + str(my_restaurant.number_served) + "人")
my_restaurant.increment_number_served(10)
print("就餐人数递增到" + str(my_restaurant.number_served) + "人")

# 尝试登录次数
my_user = User('david','beckham',45)
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print("登录次数: " + str(my_user.login_attempts))
my_user.reset_login_attempts()
print("登录次数:" + str(my_user.login_attempts))

冰淇淋小店
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def showIceCream(self):
		flavors = self.flavors
		print(flavors)

IceCream = IceCreamStand("冰淇淋小店", "好吃", ['草莓','巧克力'])
IceCream.showIceCream()

# 管理员
class Admin(User):
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges(privileges)

	def show_privileges(self):
		print(self.privileges)

my_admin = Admin('admin', 'my', 18, ['can add post', 'can delete post'])
my_admin.show_privileges()

# 权限
class Privileges():
	def __init__(self,privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

my_admin = Admin('admin', 'my', 18, ['can add post', 'can delete post'])
my_admin.privileges.show_privileges()

使用 OrderedDict
from collections import OrderedDict

person_info = OrderedDict()
person_info['zhangsan'] = '165'
person_info['wangwu'] = '155'
person_info['lisi'] = '180'

for name, height in person_info.items():
	print("name is " + name.title() + " height is " + height)

# 骰子
from random import randint
class Die():
	def __init__(self, sides=6):
		self.sides = sides
	def roll_die(self):
		sides = self.sides
		x = randint(1, sides)
		print(x)

die = Die(10)
die.roll_die()