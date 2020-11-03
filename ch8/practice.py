# 消息
def display_message():
	print("本章学习函数")
display_message()

# 喜欢的图书
def favorite_book(title):
	print("One of my favorite books is " + title.title())
favorite_book('Alice in Wonderland')

# T恤
def make_shirt(font='I love Pyton', size='m'):
	print("The T-shirt size is " + size + " and font is " + font)

make_shirt('hellow', 's')
make_shirt(size = 'm', font = 'world')
make_shirt("love peace")

# 城市
def describe_city(city, country='china'):
	print(city.title() +" is in " + country.title())
describe_city('shanghai','china')
describe_city(city = 'chongqing', country = 'china')
describe_city(city = 'tokyo', country = 'japan')

# 城市名
def city_country(city, country):
	s = city.title() + " , " + country.title()
	return s
string = city_country('shanghai','china')
print(string)

# 专辑
def make_album(name, album,number=''):
	a = {}
	a['singer'] = name
	a['album'] = album
	if number:
		a['number'] = number
	return a
album = make_album('zhangsan', 'lisi')
print(album)
album = make_album('zhangsan', 'lisi', 10)
print(album)

# 用户的专辑
while True:
	print("\nPlease tell me you want make album:")
	print("(enter 'q' at any time to quit)")
	name = input("Singer name is ?")
	if name == 'q':
		break
	album = input("album is ?")
	if album == 'q':
		break
	number = input("number is ?")
	if number == 'q':
		break
	a = make_album(name,album,number)
	print(a)

# 魔术师
magicians = ['zhangsan','lisi','wuwang']
def show_magicians(magician):
	for magician in magicians:
		print(magician)

show_magicians(magicians)

# 了不起的魔术师
def make_great(magicians):
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magicians.append("the Great " + magician)
	while great_magicians:
		magicians.append(great_magicians.pop())
make_great(magicians)
print(magicians)

# 不变的魔术师
def make_great_1(magicians):
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magicians.append("the Great " + magician)
	while great_magicians:
		magicians.append(great_magicians.pop())
	return magicians
magicians_1 = make_great_1(magicians[:])
print(magicians_1)
print(magicians)

# 三明治
def make_sanwich(*toppings):
	print(toppings)
make_sanwich('鸡蛋','火腿','面包')
make_sanwich('牛肉','面包')

# 用户简介
def build_profile(first, last, **user_info):
	"""创建一个字典, 其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('blues', 'sky', 
							 location='china', 
							 field='cs',
							 language='pyton')
print(user_profile)

# 汽车
def make_car(product, model,**infos):
	car = {}
	car['product'] = product
	car['model'] = model
	for key, value in infos.items():
		car[key] = value
	return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)